from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

shop_btn = driver.find_element_by_link_text("Shop").click()

book_javaScript = driver.find_element_by_css_selector('[alt="Mastering JavaScript"]').click()
book_add = driver.find_element_by_css_selector(".single_add_to_cart_button.button.alt").click()

item_book = driver.find_elements_by_css_selector(".wpmenucart-icon-shopping-cart-0")
# item_book_text=item_book.text
# assert item_book_text=="1 item" (ошибка, в элементе отсутствует текст)

price_book = driver.find_element_by_xpath('//span[@class="amount"]')
price_book_text = price_book.text

assert price_book_text == "₹350.00"

shoppping_cart = driver.find_element_by_class_name("wpmenucart-contents").click()

subtotal_price = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal"), "₹350.00"))
print(subtotal_price)
total_price = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total"), "₹357.00"))
print(total_price)
driver.quit()
