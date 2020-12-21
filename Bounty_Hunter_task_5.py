from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Verify forgot password functionality: after the user entered email the message is shown that the email was sent

driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/partner/signin")

email_input = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys("vmv@gmail.com")

forgot_PW_button = WebDriverWait(driver, 10).until(
    (EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]//div[4]//span[1]'))))
forgot_PW_button.click()

