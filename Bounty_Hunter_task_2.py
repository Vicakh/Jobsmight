from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Verify signing up as an bounty

driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/partner/signup")
# enter your first name
first_name = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "firstName"))))
first_name.send_keys("Big")
# enter your last name
last_name = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "lastName"))))
last_name.send_keys("Mike")
# enter your email
email_input = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys("vmv@gmail.com")
# enter password
password = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "password"))))
password.send_keys("123456T")
# click Next button
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
'//*[@id="content"]/div//div[2]/button[2]/span[1]')))
next_button.click()

recruit_experience_field = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.NAME, "recruitingExperience"))))
recruit_experience_field.click()

recruit_experience_field_option = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//option[contains(@value,'1')]"))))
recruit_experience_field_option.click()

check_box_field = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//span[@class='MuiIconButton-label']"))))
check_box_field.click()

close_button = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Close')]"))))
close_button.click()

sign_up_button = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Sign up')]"))))
sign_up_button.click()

driver.quit()