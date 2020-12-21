from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Verify on sign up if the password doesn't meet requirements there error message will be shown

driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/partner/signup")

first_name = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "firstName"))))
first_name.send_keys("Big")

last_name = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "lastName"))))
last_name.send_keys("Mike")

email_input = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys("vmm@gmail.com")

password = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "password"))))
password.send_keys("1")

next_button = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH,
'//*[@id="content"]/div//div[2]/button[2]/span[1]'))))
next_button.click()

error_notification = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]//p'))))
assert error_notification.text == "Password must be atleast 6 characters!"

# There is a bug here. PW doesn't meet requirements, but user able to sign up