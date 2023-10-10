import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')

# Chargement des identifiants à partir du fichier JSON
with open('credentials.json') as f:
    credentials = json.load(f)
USERNAME = credentials['username']
PASSWORD = credentials['password']

# Renseigner l'URL de connexion
LOGIN_URL = 'https://ecole-ipssi.ymag.cloud/index.php/login/'

print("Début du script")

try:
    print("Lancement du navigateur...")
    driver = webdriver.Chrome(options=options)
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
        sign_button = driver.find_element(By.NAME, "btn btn-primary btn-submit js-btn-signer")
        sign_button.click()
        time.sleep(5)
        sign_button.click()           
        break
    except:
        print("Bouton 'signer' non trouvé. Rechargement de la page...")
        driver.refresh()  # Recharge la page
        time.sleep(10)
        
while True:
    try:
        enregister_button = driver.find_element(By.NAME, "btn btn-primary btn-submit js-enregistrer-signature")
        enregister_button.click()
        time.sleep(5)
        enregister_button.click()           
        break
    except:
        time.sleep(10)

print("Fin du script")

driver.quit()   # Ferme le navigateur

