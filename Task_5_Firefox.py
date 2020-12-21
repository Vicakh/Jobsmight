# Verify forgot password functionality: after the user entered email the message is shown that the email was sent

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://jobmight.com/session/emp/signin")

# enter your email
email_input_field = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("vvm@gmail.com")

# click Forgot password button
forgot_PW_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]//div[2]/form/div[4]/button/span[1]')))
forgot_PW_button.click()

# enter your email next to Reset Password field
# //*[@id="content"]/div/div/div/div/div[2]/div/form/div[1]/div/div/input
email_input_field = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("vvm@gmail.com")

# click Reset Password button
# xpath //*[@id="content"]//button[1]/span[1]
reset_PW_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]//button[1]/span[1]')))
reset_PW_button.click()

# The code is running properly, but "reset password" function doesn't work. Text "Please try again." pops up