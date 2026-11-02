# Mise en ligne sur PythonAnywhere

Remplacez `VOTRE_LOGIN` par votre identifiant PythonAnywhere.

> **Bon à savoir** : un compte gratuit PythonAnywhere n'a droit qu'à **un seul site**
> (`VOTRE_LOGIN.pythonanywhere.com`). Si la gestion immo l'occupe déjà, il faut soit un
> compte payant qui autorise un 2e site, soit un 2e compte gratuit avec un autre identifiant
> (le site sera alors `AUTRE_LOGIN.pythonanywhere.com`).

## 1. Récupérer le code (console Bash)

Dans l'onglet **Consoles**, ouvrez une console **Bash** :

```
git clone https://github.com/FabH69/commande-balles.git
cd commande-balles
mkvirtualenv --python=/usr/bin/python3.12 balles
pip install -r requirements.txt
```

## 2. Préparer la base

Toujours dans la console (le virtualenv `balles` est actif) :

```
python manage.py migrate
python manage.py createsuperuser
DJANGO_DEBUG=0 python manage.py collectstatic --noinput
```

## 3. Créer le site (onglet Web)

1. **Add a new web app** → *Manual configuration* (pas « Django ») → **Python 3.12**.
2. Section **Code** :
   - *Source code* : `/home/VOTRE_LOGIN/commande-balles`
   - *Working directory* : `/home/VOTRE_LOGIN/commande-balles`
3. Section **Virtualenv** : `/home/VOTRE_LOGIN/.virtualenvs/balles`
4. Section **Static files** : URL `/static/` → dossier `/home/VOTRE_LOGIN/commande-balles/staticfiles`
5. Cliquez sur le lien du **WSGI configuration file**, effacez tout et collez :

```python
import os
import sys

chemin = "/home/VOTRE_LOGIN/commande-balles"
if chemin not in sys.path:
    sys.path.insert(0, chemin)

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"
os.environ["DJANGO_DEBUG"] = "0"
os.environ["DJANGO_ALLOWED_HOSTS"] = "VOTRE_LOGIN.pythonanywhere.com"
os.environ["DJANGO_SECRET_KEY"] = "COLLEZ-ICI-UNE-LONGUE-CHAINE-ALEATOIRE"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

   Pour générer la clé secrète, dans la console :
   `python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"`

6. Cliquez sur **Reload** en haut de l'onglet Web, puis ouvrez `https://VOTRE_LOGIN.pythonanywhere.com`.

## Mettre à jour plus tard

```
cd ~/commande-balles
git pull
workon balles
pip install -r requirements.txt
python manage.py migrate
DJANGO_DEBUG=0 python manage.py collectstatic --noinput
```

Puis **Reload** dans l'onglet Web.

## Sauvegarde

Toutes les données sont dans `~/commande-balles/db.sqlite3`. Téléchargez ce fichier de
temps en temps depuis l'onglet **Files**.
