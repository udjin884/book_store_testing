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
book_THML = driver.find_element_by_css_selector('[alt="Mastering HTML5 Forms"]').click()

book_name = driver.find_element_by_css_selector('[itemprop="name"]')
book_name_text = book_name.text
assert book_name_text == "HTML5 Forms"
print(book_name_text)
driver.quit()
