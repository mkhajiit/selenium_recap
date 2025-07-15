# selenium 설치 테스트
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()

def test_first(driver):
  assert driver.current_url == "https://www.saucedemo.com/"
  time.sleep(2)
