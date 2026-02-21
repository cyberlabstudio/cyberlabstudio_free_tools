# 📄 FICHE TECHNIQUE — update.sh.md

## Description

Ce script met à jour le système Linux en une seule commande.

Il permet de :

* mettre à jour la liste des paquets disponibles

* installer les mises à jour système

* nettoyer les paquets obsolètes

* afficher un résumé des opérations effectuées

Il simplifie la maintenance du système et garantit un environnement à jour.

## Utilisation

```bash
./update.sh [options]
```

## Options

| Option | Description |
|--------|-------------|
| `--upgrade` | Installe les mises à jour disponibles (`apt upgrade`) |
| `--full` | Effectue une mise à jour complète (`apt full-upgrade`) |
| `--clean` | Supprime les paquets inutiles après la mise à jour (`apt autoremove` + `apt autoclean`)|
| `--verbose` | Affiche les détails des opérations |

## Exemples

Mettre à jour la liste des paquets et installer les mises à jour :

```bash
./update.sh --upgrade
```

Effectuer une mise à jour complète :

```bash
./update.sh --full
```

Mettre à jour et nettoyer les paquets obsolètes :

```bash
./update.sh --upgrade --clean
```

Afficher les opérations en détail :

```bash
./update.sh --verbose
```

## Dépendances

* `apt`

* `sudo` (selon les opérations effectuées)

Ces commandes doivent être disponibles sur le système.

## Notes

* Le script nécessite généralement les droits `sudo`.

* Compatible Debian, Ubuntu et distributions basées sur APT.

* L’option `--full` peut modifier ou supprimer certains paquets selon les dépendances.

* Le nettoyage (`--clean`) supprime uniquement les paquets devenus inutiles.
