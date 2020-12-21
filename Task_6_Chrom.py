# Verify on sign up if the password doesn't meet requirements there error message will be shown

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/emp/signup")

# enter your email
email_input_field = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("vvm@gmail.com")

# enter company name
company_name = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "companyName"))))
company_name.send_keys("VVM")

# enter password which doesn't meet requirements
password = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "password"))))
password.send_keys("12345")

# enter your full name
your_full_name = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "yourName"))))
your_full_name.send_keys("Big Mike")

# a pop up warning "Password must be at least 6 characters!"
popup_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]//div/p')))
assert popup_text.text == "Password must be at least 6 characters!"

driver.quit()