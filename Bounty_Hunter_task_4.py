from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Verify login with existing email but incorrect password will prompt a pop-up saying that credentials is not valid

driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/partner/signin")

driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/partner/signin")

email_input = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys("vmv@gmail.com")

password_input = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "password"))))
password_input.send_keys("123")

popup_window = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/p")))
assert popup_window.text == "Invalid credentials, could not log you in."

#popup_window = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-gutterBottom']")))
#assert popup_window.text == "Invalid credentials, could not log you in."

login_button = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))))
login_button.click()

# driver.quit()