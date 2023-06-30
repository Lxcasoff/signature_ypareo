import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

os.environ["webdriver.chrome.driver"] = "/usr/local/bin/chromedriver"
webdriver_service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=webdriver_service)

LOGIN_URL = 'https://ecole-ipssi.ymag.cloud/index.php/login/'
USERNAME = ''
PASSWORD = ''

print("Début du script")

try:
    print("Lancement du navigateur...")
    driver = webdriver.Chrome(service=webdriver_service)
    print("Navigateur lancé.")
except Exception as e:
    print("Une erreur s'est produite lors du lancement du navigateur.")
    print(e)
    exit()

try:
    print("Aller à la page de connexion...")
    driver.get(LOGIN_URL)
    time.sleep(5)  # Attend 5 secondes pour que la page se charge
    print("Page de connexion atteinte.")
except Exception as e:
    print("Une erreur s'est produite lors de la navigation vers la page de connexion.")
    print(e)
    exit()

try:
    print("Tentative de connexion...")
    username_input = driver.find_element(By.NAME, 'login')
    password_input = driver.find_element(By.NAME, 'password')
    username_input.send_keys(USERNAME)
    time.sleep(2)  # Attend 2 secondes pour que les informations soient traitées
    password_input.send_keys(PASSWORD)
    time.sleep(2)  # Attend 2 secondes pour que les informations soient traitées

    login_button = driver.find_element(By.NAME, "btnSeConnecter")
    login_button.click()
    time.sleep(5)  # Attend 5 secondes pour que la connexion soit établie
    print("Connexion réussie.")
except Exception as e:
    print("Une erreur s'est produite lors de la tentative de connexion.")
    print(e)
    exit()
    
while True:
        try:
            sign_button = driver.find_element(By.NAME, "sign_button")
            sign_button.click()
            time.sleep(5)      
            sign_button.click()           
            break
        except:
            time.sleep(10)

print("Fin du script")
