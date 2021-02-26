from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Crear una sesión de Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# Acceder a la aplicación web
driver.get("http://www.google.com")

# Localizar cuadro de texto
#search_field = driver.find_element_by_id("lst-ib")
search_field = driver.find_element_by_name("q")
search_field.clear()

# Indicar y confirmar término de búsqueda
search_field.send_keys("neanderthal")
search_field.submit()