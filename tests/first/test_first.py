# selenium 설치 테스트
from helper.login import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login(driver):
   login(driver,"standard_user","secret_sauce")

   wait = WebDriverWait(driver, 10)
   logo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "app_logo")))

   time.sleep(2)

   # 로그인 후 로고가 화면에 존재하는지 판단
   assert logo.is_displayed()

def test_by_class(driver):
   username_input = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Username"]')
   username_input.send_keys("standard_user")

   password_input = driver.find_element(By.CSS_SELECTOR, '.login-box input[placeholder="Password"]')
   password_input.send_keys("secret_sauce")

   driver.find_element(By.CSS_SELECTOR,'.login-box .submit-button.btn_action').click()
   wait = WebDriverWait(driver, 10)
   logo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "app_logo")))

   time.sleep(2)

   assert logo.is_displayed()
   

# def test_xpath(driver):
#     driver.find_element(By.XPATH,"//input[contains(@class, 'input_error') and contains(@class, 'form_input')]").send_keys("standard_user")
#     # //input[...] 모든 input 태그에서 조건 만족하는 요소를 찾기
#     time.sleep(2)