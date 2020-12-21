import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://jobmight.com/")

# 1.Check JobsMight Logo on the footer
def verifyLogo():
    JobsMight_logo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]//header/div/div/div/div/div/div[1]')))
    assert JobsMight_logo.text == "JobsMight"
    JobsMight_logo.click()
    time.sleep(5)

# 2.Check the following buttons on the footer: Fast Feedback. Accountable Hiring.
Fast_Feedback_Acc_Hiring_logo = driver.find_element_by_xpath('//*[@id="first-txt"]/h6')
assert Fast_Feedback_Acc_Hiring_logo.text == "Fast Feedback.\nAccountable Hiring."
Fast_Feedback_Acc_Hiring_logo.click()
time.sleep(5)

# 3.Check the following buttons on the footer: Terms
terms_link = WebDriverWait(driver, 10).until(
     (EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]//div[1]/div/ul/li[1]/a'))))
assert terms_link.text == "Terms"
terms_link.click()
time.sleep(5)

# 4.Check the following buttons on the footer: Privacy
privacy_link = WebDriverWait(driver, 10).until(
     (EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]//div[1]/div/ul/li[2]/a'))))
assert privacy_link.text == "Privacy"
privacy_link.click()
time.sleep(5)

# 5.Check the following buttons on the footer: About
about_link = WebDriverWait(driver, 10).until(
     (EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]//div[1]/div/ul/li[3]/a'))))
assert about_link.text == "About"
about_link.click()
time.sleep(5)

# 6.Check the following buttons on the footer: EMPLOYER RESOURCES
EMPLOYER_RESOURCES_logo = WebDriverWait(driver, 10).until(
     (EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]//div/div/div/div[2]//h3'))))
assert EMPLOYER_RESOURCES_logo.text == "EMPLOYER\nRESOURCES"
time.sleep(5)

# 7.Check the following buttons on the footer: Quick Start
quick_start_link = WebDriverWait(driver, 10).until(
     (EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]//div[2]/div//li[1]/a'))))
assert quick_start_link.text == "Quick Start"
quick_start_link.click()
time.sleep(5)

# 8.Check the following buttons on the footer: Pricing
pricing_link = WebDriverWait(driver, 10).until(
     (EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]//div[2]/div/ul/li[2]/a'))))
assert pricing_link.text == "Pricing"
pricing_link.click()
time.sleep(5)

# 9.Check the following buttons on the footer:*NEW* Bounties
new_bounties_link = WebDriverWait(driver, 10).until(
     (EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]//div[2]/div/ul/li[3]/a'))))
assert new_bounties_link.text == "*NEW* Bounties"
new_bounties_link.click()