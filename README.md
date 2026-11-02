# Commandes groupées de balles de tennis

Petit site pour gérer les commandes groupées de balles :

- **Joueurs** : nom, téléphone, e-mail, club.
- **Commandes** : prix de la boîte, % de commission, date limite, lieu de remise.
- **Qui prend combien** : on ajoute les joueurs à la commande avec leur nombre de boîtes ;
  le site calcule le total de boîtes à commander, le montant et la commission.
- **Suivi** : payé / prévenu / remis pour chaque joueur.
- **Messages « balles arrivées »** : quand la commande passe en « Reçue », la page
  *Prévenir les joueurs* prépare un message personnalisé pour chacun (boutons WhatsApp,
  SMS, e-mail) et un récapitulatif à coller dans le groupe WhatsApp.

## Lancer en local

```
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py createsuperuser
.venv/bin/python manage.py donnees_demo   # facultatif : données fictives
.venv/bin/python manage.py runserver
```

Puis ouvrir http://127.0.0.1:8000/ et se connecter avec le compte créé.

Mise en ligne sur PythonAnywhere : voir [DEPLOIEMENT.md](DEPLOIEMENT.md).
