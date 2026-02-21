# 📄 FICHE TECHNIQUE — `clean.sh.md`

## Description

Ce script nettoie les fichiers temporaires et les caches inutiles du système.

Il permet de :

* supprimer les fichiers temporaires dans `/tmp`

* nettoyer les caches utilisateurs dans `~/.cache`

* supprimer certains fichiers résiduels générés par des applications

* libérer de l’espace disque sans risque pour les données personnelles

Il simplifie l’entretien régulier du système Linux.

## Utilisation

```bash
./clean.sh [options]
```

## Options

| Option | Description |
|--------|-------------|
| `--dry-run` | Affiche les fichiers qui seraient supprimés sans les effacer |
| `verbose` | Affiche en détail les fichiers supprimés |

## Exemples

Nettoyage standard :

```bash
./clean.sh
```

Nettoyage détaillé :

```bash
./clean.sh --verbose
```

Simulation sans suppression :

```bash
./clean.sh --dry-run
```

## Dépendances

* `rm`

* `du` (selon les variantes du script)

Ces commandes sont disponibles par défaut sur toutes les distributions Linux.

## Notes

* Certaines suppressions peuvent nécessiter `sudo`.

* Aucun fichier personnel n’est supprimé.

* Compatible avec toutes les distributions Linux.

* Certains caches seront recréés automatiquement par les applications.
