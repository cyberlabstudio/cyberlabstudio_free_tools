# 📄 FICHE TECHNIQUE — `sync.sh.md`

## Description

Ce script synchronise deux dossiers en utilisant `rsync`.

Il permet de :

* synchroniser un dossier source vers un dossier de destination

* copier uniquement les fichiers modifiés

* préserver les permissions et attributs

* afficher un résumé des transferts

* effectuer une synchronisation en mode simulation

Il simplifie la mise à jour de dossiers locaux ou distants sur les systèmes Linux.

## Utilisation

```bash
./sync.sh <source> <destination> [options]
```

* `<source>` : dossier à synchroniser

* `<destination>` : dossier cible

## Options

| Option | Description |
|--------|-------------|
| `--delete` | Supprime dans la destination les fichiers absents de la source |
| `--dry-run` | Simule la synchronisation sans modifier les fichiers |
| `--verbose` | Affiche les fichiers transférés en détail |
| `--archive` | Active le mode archive (`-a`) pour préserver permissions, dates, liens, etc. |

## Exemples

Synchronisation standard :

```bash
./sync.sh ~/Documents ~/Backup/Documents
```

Synchronisation avec suppression des fichiers obsolètes :

```bash
./sync.sh ~/projet ~/Backup/projet --delete
```

Simulation sans rien modifier :

```bash
./sync.sh ~/site ~/Backup/site --dry-run
```

Synchronisation détaillée :

```bash
./sync.sh ~/scripts ~/Backup/scripts --verbose
```

## Dépendances

* `rsync`

Cette commande doit être installée sur le système.

## Notes

* Le script ne modifie jamais la source, uniquement la destination.

* L’option `--delete` doit être utilisée avec précaution.

* Compatible avec toutes les distributions Linux.

* Le mode `--archive` est recommandé pour les sauvegardes complètes.
