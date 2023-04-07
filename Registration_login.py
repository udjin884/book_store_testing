from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

my_account_btn = driver.find_element_by_link_text("My Account").click()
email_reg = driver.find_element_by_id("reg_email")
email_reg.send_keys("Test12347@mail.ru")
password = driver.find_element_by_id("reg_password")
password.send_keys("Test12347@mail.ru")

register_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="register"]')))
register_btn.click()
driver.quit()
