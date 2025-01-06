from selenium import webdriver

username = "guest"
password = "welcome2qauto"
url = f"https://{username}:{password}@qauto2.forstudy.space/"
driver = webdriver.Chrome()
driver.get(url)

xpaths = [
    "//button[contains(@class, 'header_signin') and text()='Sign In']",
    "//button[contains(@class, 'hero-descriptor_btn') and text()='Sign up']",
    "//a[contains(@class, 'header-link') and text()='Home']",
    "//button[@appscrollto='aboutSection' and contains(@class, 'header-link') and text()='About']",
    "//input[@type='text' and @name='email' and @id='signinEmail' and @formcontrolname='email']",
    "//input[@type='password' and @name='password' and @id='signinPassword' and @formcontrolname='password']",
    "//input[@type='checkbox' and @name='remember' and @id='remember' and @formcontrolname='remember']",
    "//button[contains(@class, 'header-link') and contains(@class, '-guest') and text()='Guest log in']",
    "//button[@id='userNavDropdown' and contains(@class, 'user-nav_toggle') and text()[contains(., 'My profile')]]",
    "//a[@routerlink='/panel/garage' and text()='Garage']",
    "//a[@routerlink='/panel/expenses' and text()='Fuel expenses']",
    "//button[@id='carSelectDropdown' and contains(@class, 'car-select-dropdown_toggle') and contains(@class, 'btn') and contains(@class, 'btn-secondary') and text()='Audi TT']",
    "//a[@routerlink='/panel/instructions' and contains(@class, 'disabled') and text()='Instructions']",
    "//a[@class='instruction-link_download' and @href='https://qauto2.forstudy.space/public/instructions/audi/tt/Front windshield wipers on Audi TT.pdf']",
    "//button[contains(@class, 'user-nav_link') and text()='Logout']",
    "//button[contains(@class, 'btn') and contains(@class, 'btn-primary') and text()='Add car']",
    "//select[@id='addCarBrand' and @formcontrolname='brand']",
    "//select[@id='addCarModel' and @formcontrolname='model']",
    "//input[@id='addCarMileage' and @formcontrolname='mileage']",
    "//span[@class='icon icon-edit']",
    "//span[@class='icon icon-calendar']",
    "//span[@class='socials_icon icon icon-instagram']",
    "//div[@class='ytp-cued-thumbnail-overlay-image' and contains(@style, 'background-image: url('https://i.ytimg.com/vi_webp/znjjC0Iw8Wc/maxresdefault.webp')')]",
    "//button[@class='ytp-large-play-button ytp-button ytp-large-play-button-red-bg' and @aria-label='Смотреть']",
    "//path[@d='M16.8847 66.3337C19.7898 64.5503 22.5268 63.23 24.7305 62.1758C28.2581 60.4817 31.2877 59.0151 33.5433 56.6223C44.6137 44.8919 41.7978 26.8706 41.6754 26.1089L41.3642 24.2483L40.4698 25.918C40.4241 26.0074 35.4316 35.217 26.6831 41.6094C25.6913 42.3264 24.4711 43.1328 23.0331 44.0794C20.3999 45.8181 17.113 47.9753 13.1559 51.01C0.149404 60.9976 0 77.5239 0 78.2226V80L1.14751 78.6167C1.15996 78.5903 5.62133 73.2582 16.8847 66.3337Z' and @fill='#54D226']"
]

css_selectors = [
    "button.btn.btn-outline-white.header_signin",
    "button.hero-descriptor_btn.btn.btn-primary",
    "a.btn.header-link.-active",
    "button.btn.header-link[appscrollto='aboutSection']",
    "input#signinEmail.form-control[name='email'][formcontrolname='email']",
    "input#signinPassword.form-control[name='password'][formcontrolname='password']",
    "input#remember.form-check-input[name='remember'][formcontrolname=['remember']",
    "button.header-link.-guest"
    "button#userNavDropdown.dropdown-toggle.user-nav_toggle"
    "a.dropdown-item.user-nav_link[href='/panel/garage']",
    "a.dropdown-item.user-nav_link[href='/panel/expenses']",
    "button#carSelectDropdown.car-select-dropdown_toggle.btn.btn-secondary",
    "a.dropdown-item.user-nav_link.disabled[href='/panel/instructions']",
    "a.instruction-link_download[href='https://qauto2.forstudy.space/public/instructions/audi/tt/Front windshield wipers on Audi TT.pdf']",
    "button.dropdown-item.user-nav_link",
    "button.btn.btn-primary",
    "select#addCarBrand.form-control[formcontrolname='brand']",
    "select#addCarModel.form-control[formcontrolname='model']",
    "input#addCarMileage.form-control[formcontrolname='mileage']",
    "span.icon.icon-edit",
    "span.icon.icon-calendar",
    "span.socials_icon.icon.icon-instagram",
    "div.ytp-cued-thumbnail-overlay-image[style*='background-image: url('https://i.ytimg.com/vi_webp/znjjC0Iw8Wc/maxresdefault.webp')']",
    "button.ytp-large-play-button.ytp-button.ytp-large-play-button-red-bg[aria-label='Смотреть']",
    "path[d='M16.8847 66.3337C19.7898 64.5503 22.5268 63.23 24.7305 62.1758C28.2581 60.4817 31.2877 59.0151 33.5433 56.6223C44.6137 44.8919 41.7978 26.8706 41.6754 26.1089L41.3642 24.2483L40.4698 25.918C40.4241 26.0074 35.4316 35.217 26.6831 41.6094C25.6913 42.3264 24.4711 43.1328 23.0331 44.0794C20.3999 45.8181 17.113 47.9753 13.1559 51.01C0.149404 60.9976 0 77.5239 0 78.2226V80L1.14751 78.6167C1.15996 78.5903 5.62133 73.2582 16.8847 66.3337Z'][fill='#54D226']"
]

for xpath in xpaths:
    print(f"XPath: {xpath}")
for css in css_selectors:
    print(f"CSS: {css}")

driver.quit()
