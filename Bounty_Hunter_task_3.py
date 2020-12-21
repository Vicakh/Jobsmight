from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Verify login with not existing email will prompt a pop-up saying that they should sign up

driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/partner/signin")

email_input = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys("123@gmail.com")

password_input = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "password"))))
password_input.send_keys("123456T")

login_button = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))))
login_button.click()

popup_window = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body//div//p")))
assert popup_window.text == "Email does not exist. Please signup."

driver.quit()