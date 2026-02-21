# 📄 FICHE TECHNIQUE — `backup.sh.md`

## Description

Ce script crée une sauvegarde compressée d’un dossier ou d’un fichier.
Il permet de :

* sauvegarder un répertoire complet

* compresser la sauvegarde au format `.tar.gz`

* conserver une copie datée

* automatiser des sauvegardes régulières

Il simplifie la création d’archives de sauvegarde sur les systèmes Linux.

## Utilisation

```bash
./backup.sh <source> <destination> [options]
```

* `<source>` : fichier ou dossier à sauvegarder

* `<destination>` : dossier où stocker l’archive générée

## Options

| Option | Description |
|--------|-------------|
| `--name` | Définit un nom personnalisé pour l’archive |
| `--no-date` | Désactive l’ajout automatique de la date dans le nom |
| `--verbose` | Affiche les fichiers ajoutés à l’archive |

## Exemples

Créer une sauvegarde standard du dossier `~/Documents` :

```bash
./backup.sh ~/Documents ~/Backups
```

Créer une sauvegarde avec un nom personnalisé :

```bash
./backup.sh ~/projet ~/Backups --name projet_v1
```

Créer une sauvegarde sans date dans le nom :

```bash
./backup.sh ~/site ~/Backups --no-date
```

## Dépendances

* `tar`

* `gzip`

Ces commandes sont disponibles par défaut sur la majorité des distributions Linux.

## Notes

* Le script crée automatiquement le dossier de destination s’il n’existe pas.

* Les sauvegardes sont compressées au format `.tar.gz`.

* Compatible avec toutes les distributions Linux.

* Le nom final de l’archive inclut la date, sauf si `--no-date` est utilisé.
