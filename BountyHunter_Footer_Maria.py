import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://jobmight.com/")

def verifyLogo():

# Check JobsMight Logo on the footer
    JobsMight_logo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]//header/div/div/div/div/div/div[1]')))
    assert JobsMight_logo.text == "JobsMight"

time.sleep(5)
#fast_feedback_logo = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, '//*[@id="first-txt"]/h6'))))
#assert fast_feedback_logo.text == "Fast Feedback. Accountable Hiring"
terms_logo = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div//div[2]/header//div/div/div[1]/div/ul/li[1]'))))
assert terms_logo.text == "Terms"
terms_logo.click()
time.sleep(5)
privacy_term = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[2]/header//div/div[1]/div/ul/li[2]'))))
assert privacy_term.text == "Privacy"
privacy_term.click()
time.sleep(5)
About_term = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[2]/header//div[1]/div/ul/li[3]'))))
assert About_term.text == "About"
About_term.click()
time.sleep(5)
EMPLOYER_RESOURCES = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div//div[2]/header/div//div[2]/div'))))
EMPLOYER_RESOURCES.text == "EMPLOYER_RESOURCES"
EMPLOYER_RESOURCES.click()
time.sleep(5)
Quick_Start = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/header//div//div[3]/div/ul/li[1]'))))
Quick_Start.text == "Quick Start"
Quick_Start.click()
time.sleep(5)
Pricing_field = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div//div[2]/header/div//div[2]/div/ul/li[2]'))))
Pricing_field.text =="Pricing"
Pricing_field.click()
time.sleep(5)
NEW_Bounties = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div//div[2]/header//div//div[2]/div/ul/li[3]'))))
NEW_Bounties.text == "*NEW* Bounties"
NEW_Bounties.click()
time.sleep(5)
#driver.quit()