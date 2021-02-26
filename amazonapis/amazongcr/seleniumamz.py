from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Crear una sesión de Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# Acceder a la aplicación web
driver.get("http://amazon.com/portal-migration/gc/redeem")

#Fill in e-mail
email_field = driver.find_element_by_name("email")
email_field.clear()
email_field.send_keys("lucioric2000@gmail.com")

#Fill in pasword
password_field = driver.find_element_by_name("password")
password_field.clear()
password_field.send_keys("wl8m5tNk")

#Submits the sign-in form
sign_in_submit_button = driver.find_element_by_id("signInSubmit")
sign_in_submit_button.submit()
