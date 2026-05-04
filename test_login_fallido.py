from selenium import webdriver
from login_page import LoginPage

driver = webdriver.Chrome()

login = LoginPage(driver)

login.abrir()
login.login("locked_out_user", "secret_sauce")

error = login.obtener_error()

if "locked out" in error:
    print("Error validado correctamente")
else:
    print("Error no detectado")

driver.quit()