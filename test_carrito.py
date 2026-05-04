from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

login = LoginPage(driver)

login.abrir()
login.login("standard_user", "secret_sauce")

wait.until(EC.visibility_of_element_located((By.ID, "inventory_container")))

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

carrito = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
).text

if carrito == "1":
    print("Producto agregado al carrito")
else:
    print("Error")

driver.quit()