from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

logout_btn = driver.find_element_by_link_text("Logout")
logout_btn_text = logout_btn.text
assert logout_btn_text == "Logout"
print(logout_btn_text)

logout_btn=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.LINK_TEXT,"Logout")))
logout_btn.click()
driver.quit()



