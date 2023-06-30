
# Script de signature automatique

Ce script en Python permet de se connecter à un site web, remplir les informations de connexion et effectuer une signature automatique en cliquant sur un bouton spécifique.

## Prérequis

Avant de pouvoir exécuter le script, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3 : [Téléchargement de Python](https://www.python.org/downloads/)
- ChromeDriver : [Téléchargement de ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

## Installation

1. Clonez ce dépôt GitHub sur votre machine :

   ```
   git clone https://github.com/Lxcasoff/signature_ypareo.git
   ```

2. Accédez au répertoire du projet :

   ```
   cd signature_ypareo
   ```
   
   
3. Installation prerequis
```
brew install python3
brew install pip 
brew install chromium-chromedriver
pip install selenium
```

## Configuration

Avant de lancer le script, vous devez configurer certaines variables dans le fichier `signature.py` :

- `LOGIN_URL` : l'URL de la page de connexion.
- `USERNAME` : votre nom d'utilisateur pour vous connecter.
- `PASSWORD` : votre mot de passe pour vous connecter.

## Exécution

Pour lancer le script, exécutez la commande suivante :

```
python3 signature.py
```





