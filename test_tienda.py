import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service('/usr/bin/chromedriver'),
        options=options
    )

    yield driver
    driver.quit()


def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)

    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url


def test_login_fallido(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)

    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.obtener_error()