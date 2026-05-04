from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # LOGIN
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    if "inventory" in driver.current_url:
        print("Login exitoso")

    # CARRITO
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    print("Carrito:", carrito)

    # LOGIN FALLIDO
    driver.delete_all_cookies()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    print("Error:", error)

except Exception as e:
    print("Error:", e)

finally:
    time.sleep(3)
    driver.quit()