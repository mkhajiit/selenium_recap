# selenium 설치 테스트
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()

def test_login(driver):
   driver.find_element(By.ID,'user-name').send_keys("standard_user")
   driver.find_element(By.ID,'password').send_keys("secret_sauce")

   driver.find_element(By.ID,"login-button").click()

   time.sleep(2)

   assert driver.current_url == "https://www.saucedemo.com/inventory.html"
