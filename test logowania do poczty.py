from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://profil.wp.pl/login/login.html"
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")

login= "hubert.szelewa@wp.pl"
hasło= "123"

driver.get(url)
driver.maximize_window()

try:
    akcept_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='AKCEPTUJĘ I PRZECHODZĘ DO SERWISU']")))
    akcept_button.click()
except:
    print('błąd przy akceptowaniu cookies')


try:
    driver.find_element(By.ID, "login").send_keys(login)
    sleep(3)
except:
    print('błąd przy wpisywaniu loginu')

try:
    driver.find_element(By.ID, "password").send_keys(hasło)
    sleep(3)
except:
    print('błąd przy wpisywaniu hasła')

driver.find_element(By.ID, "stgMain").click()
sleep(5)


print('koniec testu')

#dodanie asercji sprawdzającego poprawne zalogowanie