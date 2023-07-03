
# Script de signature automatique

Ce script en Python permet de se connecter à un site web, remplir les informations de connexion et effectuer une signature automatique en cliquant sur un bouton spécifique.

## Prérequis

- MacOS

Avant de pouvoir exécuter le script, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3 : [Téléchargement de Python](https://www.python.org/downloads/)
- ChromeDriver : [Téléchargement de ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

## Installation

1. Installation prerequis
```
brew install python3
brew install pip 
brew install chromium-chromedriver
pip install selenium
```

2. Clonez ce dépôt GitHub sur votre machine :

```
git clone https://github.com/Lxcasoff/signature_ypareo.git
```

3. Accédez au répertoire du projet :

```
cd signature_ypareo
```

   


## Configuration

Avant de lancer le script, vous devez configurer certaines variables dans le fichier `signature.py` :

```python
LOGIN_URL = ''
USERNAME = ''
PASSWORD = ''
```

## Exécution

Pour lancer le script, exécutez la commande suivante :

```
python3 signature.py
```





