from selenium.webdriver.common.by import By

def login(driver,username,password):
  driver.find_element(By.ID,'user-name').send_keys(username)
  driver.find_element(By.ID,'password').send_keys(password)
  driver.find_element(By.ID,"login-button").click()