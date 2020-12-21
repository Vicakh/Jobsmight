from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Verify successful login when the bounty enters valid email and password

driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/partner/signin")

email_input = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys("vmv@gmail.com")

password_input = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "password"))))
password_input.send_keys("123456T")

login_button = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))))
login_button.click()

driver.quit()