import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.maximize_window()

shop_btn = driver.find_element_by_link_text("Shop").click()

driver.execute_script("window.scrollBy(0, 300);")

book_add = driver.find_element_by_css_selector(
    ".button.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()
time.sleep(3)
shoppping_cart = driver.find_element_by_class_name("wpmenucart-contents").click()
time.sleep(3)
delete_book=driver.find_element_by_css_selector('[title="Remove this item"]').click()
time.sleep(3)
undo_btn=driver.find_element_by_css_selector(".woocommerce-message a").click()

quantify_del = driver.find_element_by_css_selector('.input-text.qty.text').clear()

quantify_add = driver.find_element_by_css_selector('.input-text.qty.text')
quantify_add.send_keys("3")
time.sleep(3)

update_basket_btn = driver.find_element_by_css_selector('[name="update_cart"]').click()
time.sleep(3)

quantify_book = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,'[value="3"]'),"3"))
print(quantify_book)
time.sleep(3)
apply_coupon_btn=driver.find_element_by_css_selector('[name="apply_coupon"]').click()

coupon_mesage=WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-error li"),"Please enter a coupon code."))
print(coupon_mesage)
driver.quit()