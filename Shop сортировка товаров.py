from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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

default_select = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".orderby"), "Default sorting"))
print(default_select)

sort_price_high = driver.find_element_by_css_selector(".orderby")
select_high = Select(sort_price_high)
select_high.select_by_value("price-desc")

select_high_selected = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".orderby"), "Sort by price: high to low"))
print(select_high_selected)
# driver.quit()
