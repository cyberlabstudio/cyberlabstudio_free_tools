# 📜 Script — `useradd.sh`
**CyberLabStudio • Pack 10 Scripts Linux Gratuits**

## 🧩 Description

Ce script permet de créer un utilisateur complet en une seule commande, avec :

* Création du compte utilisateur

* Définition d’un mot de passe

* Ajout aux groupes nécessaires (ex : `sudo`)

Idéal pour les administrateurs système ou les utilisateurs avancés.

## ⚙️ Fonctionnement

### Commandes clés utilisées

```bash
sudo adduser $nom_utilisateur
sudo passwd $nom_utilisateur
sudo usermod -aG sudo $nom_utilisateur
```

### Options avancées

Le script peut utiliser `useradd` pour un contrôle plus fin :

* `--home-dir`

* `--shell`

* `--sudo` (selon ta version du script)

## 🧪 Exemples d’utilisation

* Créer un utilisateur nommé **alex** :
```bash
./useradd.sh "alex"
```

* Créer un utilisateur avec un répertoire personnel personnalisé :
```bash
./useradd.sh "alex" --home-dir "/custom/home/alex"
```

## 🚨 Notes et limitations

* **Permissions** : nécessite les droits `sudo`

* **Compatibilité** : Debian, Ubuntu, Arch

* **Sécurité** : le mot de passe est demandé interactivement

* **Vérification** : le script vérifie si l’utilisateur existe déjà

## 📌 Intégration avec d’autres scripts

* Peut être combiné avec `backup.sh` pour sauvegarder les données utilisateur

* Utilisable dans un workflow d’automatisation (déploiement, onboarding, etc.)

## 🖤 CyberLabStudio © 2026

Packs publics • Outils & Apps • Scripts Linux • Templates Notion • Ressources techniques
