from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper.login import login


def test_third_scroll(driver):
  login(driver,"standard_user","secret_sauce")
  print("로그인 함수 완료")

  # 현재 스크롤 위치 확인
  current_scroll = driver.execute_script("return window.scrollY;")

  # 맨 아래로 스크롤
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  print("스크롤 실행 됨")

  # 스크롤 후 위치 확인
  new_scroll = driver.execute_script("return window.scrollY;")

  assert new_scroll > current_scroll, "스크롤이 이동하지 않았습니다."
    
