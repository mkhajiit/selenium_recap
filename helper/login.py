from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver,username,password):
  driver.find_element(By.ID,'user-name').send_keys(username)
  driver.find_element(By.ID,'password').send_keys(password)

  driver.find_element(By.ID,"login-button").click()