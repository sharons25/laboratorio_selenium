from selenium import webdriver
from login_page import LoginPage

driver = webdriver.Chrome()

login = LoginPage(driver)

login.abrir()
login.login("standard_user", "secret_sauce")

if "inventory" in driver.current_url:
    print("Login exitoso")
else:
    print("Error")

driver.quit()