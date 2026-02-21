# 📄 FICHE TECHNIQUE — `useradd.sh.md`

## Description

Ce script crée un nouvel utilisateur Linux en une seule commande.

Il permet de :

- créer le compte utilisateur

- définir un mot de passe

- ajouter l’utilisateur à des groupes (ex : `sudo`)

- définir un répertoire personnel personnalisé (optionnel)

Il simplifie la gestion des utilisateurs sur les systèmes Linux.

## Utilisation

```bash
./useradd.sh <nom_utilisateur> [options]
```

## Options

| Option | Description |
|--------|-------------|
| `--home-dir` | Définit un répertoire personnel personnalisé |
| `--shell` | Définit un shell spécifique |
| `--sudo` | Ajoute l’utilisateur au groupe sudo (si non activé par défaut) |

## Exemples

Créer un utilisateur nommé **alex** :

```bash
./useradd.sh alex
```

Créer un utilisateur avec un répertoire personnel personnalisé :

```bash
./useradd.sh alex --home-dir /custom/home/alex
```

Créer un utilisateur avec un shell spécifique :

```bash
./useradd.sh alex --shell /bin/zsh
```

## Dépendances

* `adduser`

* `passwd`

* `usermod`

Ces commandes doivent être disponibles sur le système.

## Notes

* Nécessite les droits `sudo`.

* Compatible Debian, Ubuntu, Arch (selon les commandes disponibles).

* Le mot de passe est demandé interactivement.

* Le script vérifie si l’utilisateur existe déjà avant de le créer.
