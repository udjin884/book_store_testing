import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

shop_btn = driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 300);")

book_add = driver.find_element_by_css_selector(
    ".button.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()
time.sleep(3)
shoppping_cart = driver.find_element_by_class_name("wpmenucart-contents").click()

proceed_to_checkout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
proceed_to_checkout_btn.click()

firs_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
firs_name.send_keys("Ivan")

last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Petrov")

email = driver.find_element_by_id("billing_email")
email.send_keys("Test123@mail.ru")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("8888777666")

country = driver.find_element_by_id("select2-chosen-1").click()
input_country = driver.find_element_by_id("s2id_autogen1_search")
input_country.send_keys("Russ")
input_Russia = driver.find_element_by_id("select2-result-label-392").click()

address_steet = driver.find_element_by_id("billing_address_1")
address_steet.send_keys("Test.street")
apartament = driver.find_element_by_id("billing_address_2")
apartament.send_keys("S5D5")

town_city = driver.find_element_by_id("billing_city")
town_city.send_keys("Moscow")

state_county = driver.find_element_by_id("billing_state")
state_county.send_keys("Moscow")

post_zip = driver.find_element_by_id("billing_postcode")
post_zip.send_keys("123465")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payments = driver.find_element_by_css_selector('[for="payment_method_cheque"]').click()

place_order = driver.find_element_by_id("place_order").click()

thank_you_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
                                     "Thank you. Your order has been received."))
print(thank_you_text)

Check_Payments_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table.order_details"), "Check Payments"))
print(Check_Payments_text, "2")
driver.quit()

