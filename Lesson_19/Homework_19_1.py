import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)
if response.status_code == 200:
    photos = response.json().get('photos', [])
    if photos:
        for idx, photo in enumerate(photos, start=1):
            img_url = photo['img_src']
            img_data = requests.get(img_url).content
            with open(f"mars_photo{idx}.jpg", 'wb') as file:
                file.write(img_data)
            print(f"Фото {idx} збережено.")
    else:
        print("Немає фото для заданих параметрів.")
else:
    print(f"Помилка запиту: {response.status_code}")
