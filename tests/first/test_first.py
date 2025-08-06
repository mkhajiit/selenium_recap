# selenium 설치 테스트
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login(driver):
   driver.find_element(By.ID,'user-name').send_keys("standard_user")
   driver.find_element(By.ID,'password').send_keys("secret_sauce")

   driver.find_element(By.ID,"login-button").click()

   wait = WebDriverWait(driver, 10)
   wait.until(EC.presence_of_element_located((By.CLASS_NAME, "app_logo")))

   time.sleep(2)
   assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_xpath(driver):
    driver.find_element(By.XPATH,"//input[contains(@class, 'input_error') and contains(@class, 'form_input')]").send_keys("standard_user")
    # //input[...] 모든 input 태그에서 조건 만족하는 요소를 찾기
    time.sleep(2)