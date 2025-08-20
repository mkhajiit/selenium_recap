# 루트에서 pytest로 실행할것
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
  #옵션 설정
  chrome_options = Options()
  chrome_options.add_argument("--window-size=800,600")
  # chrome_options.add_argument("--headless")
  chrome_options.add_argument("--guest")  # 게스트 모드로 딤드처리 시키는 비밀번호 팝업 제거

  #드라이버 생성
  driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
  )
  driver.get("https://www.saucedemo.com")
  yield driver
  driver.quit()