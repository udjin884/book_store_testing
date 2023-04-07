from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
my_account_menu = driver.find_element_by_link_text("My Account").click()
user_name = driver.find_element_by_id("username")
user_name.send_keys("test123@bk.ru")
password = driver.find_element_by_id("password")
password.send_keys("test123@bk.ru")
login_btn = driver.find_element_by_name("login").click()

shop_tab = driver.find_element_by_link_text("Shop").click()
Android_Quick_Start_Guide = driver.find_element_by_css_selector('[alt="Android Quick Start Guide"]').click()
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text = book_old_price.text
book_new_price = driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text = book_new_price.text
assert book_old_price_text == "₹600.00"
assert book_new_price_text == "₹450.00"

book_img = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".attachment-shop_single")))
book_img.click()
book_img_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
book_img_close.click()
driver.quit()
