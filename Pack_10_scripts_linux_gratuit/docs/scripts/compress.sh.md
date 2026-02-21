# 📄 FICHE TECHNIQUE — compress.sh.md

## Description

Ce script compresse un fichier ou un dossier en utilisant le format `.tar.gz.`

Il permet de :

* compresser un dossier complet

* compresser un fichier unique

* réduire la taille d’un répertoire pour l’archiver ou le transférer

* générer une archive nommée automatiquement ou personnalisée

Il simplifie la création d’archives compressées sur les systèmes Linux.

## Utilisation

```bash
./compress.sh <source> <destination> [options]
```

* `<source>` : fichier ou dossier à compresser

* `<destination>` : dossier où stocker l’archive générée

## Options

| Option | Description |
|--------|-------------|
| `--name` | Définit un nom personnalisé pour l’archive |
| `--verbose` | Affiche les fichiers ajoutés à l’archive |
| `--no-date` | Désactive l’ajout automatique de la date dans le nom |

## Exemples

Compresser un dossier :

```bash
./compress.sh ~/Documents ~/Archives
```

Compresser un dossier avec un nom personnalisé :

```bash
./compress.sh ~/projet ~/Archives --name projet_final
```

Compresser un fichier sans ajouter la date :

```bash
./compress.sh notes.txt ~/Archives --no-date
```

## Dépendances

* `tar`

* `gzip`

Ces commandes sont disponibles par défaut sur la majorité des distributions Linux.

## Notes

* Le script crée automatiquement le dossier de destination s’il n’existe pas.

* Le nom final de l’archive inclut la date, sauf si `--no-date` est utilisé.

* Compatible avec toutes les distributions Linux.

* Le format généré est toujours `.tar.gz`.
