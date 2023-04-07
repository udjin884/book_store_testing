from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

my_account = driver.find_element_by_link_text("My Account").click()

username = driver.find_element_by_id("username")
username.send_keys("Test1234@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("Test1234@mail.ru")
login_btn = driver.find_element_by_css_selector('[name="login"]').click()

shop_btn = driver.find_element_by_link_text("Shop").click()
THML_btn = driver.find_element_by_link_text("HTML").click()
book_count = driver.find_elements_by_css_selector(".attachment-shop_catalog")
if len(book_count) == 3:
    print("На стринице 3 книги")
else:
    print("Не известное количество книг")
driver.quit()
