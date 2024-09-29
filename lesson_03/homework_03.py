alice_in_wonderland = ("""Would you tell me, please, which way I ought to go from here?"
                       "That depends a good deal on where you want to get to," said the Cat.
                       '"I don\'t much care where ——" said Alice.
                       '"Then it doesn\'t matter which way you go," said the Cat.
                       '"—— so long as I get somewhere," Alice added as an explanation.
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough.""")
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_area = 436402
azov_area = 37800
general_area = f'General area = {black_area + azov_area}'
print(general_area)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
pair_1 = 250449
pair_2 = 222950
general_count = 375291
store_3 = general_count - pair_1
print(f'Third store contain = {store_3}')
store_2 = pair_2 - store_3
print(f'Second store contain = {store_2}')
store_1 = pair_1 - store_2
print(f'First store contain = {store_1}')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
all_amount = monthly_payment * 18
print(f'Computer cost = {all_amount}')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print (f'a) = {8019 % 8}')
print (f'b) = {9907 % 9}')
print (f'c) = {2789 % 5}')
print (f'd) = {7248 % 6}')
print (f'e) = {7128 % 5}')
print (f'f) = {19224 % 9}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274
mid_pizza = 218
juice = 35
cake = 350
water = 21
print(f'Birthday cost = {(big_pizza * 4) + (mid_pizza * 2) + (juice * 4) + cake + (water * 3)}')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
print(f'Pages count = {all_photos // 8}')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
petrol = 9
tank = 48
general_petrol = (distance // 100) * 9
print(f'Petrol count for all trip = {general_petrol}')
print(f'Stops for refueling = {general_petrol // tank}')