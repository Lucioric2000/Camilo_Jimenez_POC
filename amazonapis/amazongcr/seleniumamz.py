from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, logging
logger = logging.getLogger(__name__)
print("stdout")
# Crear una sesión de Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# Acceder a la aplicación web
driver.get("http://amazon.com/portal-migration/gc/redeem")
#or raises selenium.common.exceptions.NoSuchElementException

class GiftCodeScraper:
    def login(self):
        #Fill in e-mail
        email_field = driver.find_element_by_name("email")
        email_field.clear()
        email_field.send_keys("username")

        #Fill in pasword
        password_field = driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys("password")

        #Submits the sign-in form
        sign_in_submit_button = driver.find_element_by_id("signInSubmit")
        sign_in_submit_button.submit()
        #after login, you should need to submit a confirmation code, then, use your login credentials or a unsecured ones
    def test_code(self, code):
        while True:
            try:
                redemption_input = driver.find_element_by_id("gc-redemption-input")#or name claimCode
            except Exception:
                logger.exception("gift code input box still not ready?")
                time.sleep(5)
            else:
                break
        redemption_input.clear()
        redemption_input.send_keys(code)

        submit_button = driver.find_element_by_id("gc-redemption-apply-button")
        #captcha ID: gc-captcha-code-input
        captchas = driver.find_elements_by_id("gc-captcha-code-input")
        #print("captchas", captchas)
        #if len(captchas) > 0:
        #    cpc = input("Enter the captcha response: ")
        #    captchas[0].clear()
        #    captchas[0].send_keys(cpc)
        #Submits the redeem code
        submit_button.submit()

        element = WebDriverWait(driver, 40).until(
                EC.presence_of_element_located((By.ID, "gc-redemption-info-message")))
        return self.discriminate_response()
    def discriminate_response(self):
        alertsucess = driver.find_elements_by_id("alertRedemptionSuccess")
        errmessages = driver.find_elements_by_id("gc-redemption-error")
        if len(errmessages):
            return {"success": False, "message": errmessages[0].text}
        else:
            return {"success": True, "message": alertsucess[0].text}
#exp = EC.presence_of_element_located((By.NAME, "email"))
#mex: L6NHW-AFMUSB-VXYGU: L6NHWAFMUSBVXYGU
#US: Y475L-TDLHQZ-TSMX3
gcs = GiftCodeScraper()

try:
    gcs.login()
    #falsetc = gcs.test_code("L6NHWAFMUSBVXYGU")
    truetc = gcs.test_code("JR6JQD38VW4KAZ")
    print("tc", truetc)
finally:
    pass
    #driver.quit()
