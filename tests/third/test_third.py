from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper.login import login


def test_third_scroll(driver):
    login(driver,"standard_user","secret_sauce")
    
