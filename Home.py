from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element_by_css_selector('.attachment-shop_catalog[title="Selenium Ruby"]').click()
reviews_btn = driver.find_element_by_css_selector(".reviews_tab>a").click()
driver.execute_script("window.scrollBy(0, 600);")
five_stars = driver.find_element_by_css_selector(".star-5").click()
my_review = driver.find_element_by_id("comment")
my_review.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Ivan")
email = driver.find_element_by_id("email")
email.send_keys("Test123@mail.ru")
submit_btn = driver.find_element_by_id("submit").click()
driver.quit()
