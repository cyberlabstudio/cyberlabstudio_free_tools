# 📄 FICHE TECHNIQUE — `sysinfo.sh.md`

## Description

Ce script affiche les informations essentielles du système.

Il permet de :

* afficher la version du système d’exploitation

* afficher les informations CPU

* afficher la quantité de mémoire disponible

* afficher l’espace disque utilisé

* afficher les informations réseau de base

Il simplifie l’obtention rapide d’un résumé complet du système Linux.

## Utilisation

```bash
./sysinfo.sh [options]
```

## Options

| Option | Description |
|--------|-------------|
| `--cpu` | Affiche uniquement les informations CPU |
| `--memory` | Affiche uniquement les informations mémoire |
| `--disk` | Affiche uniquement l’espace disque |
| `--network` | Affiche uniquement les informations réseau |
| `--all` | Affiche toutes les informations (mode par défaut) |

## Exemples

Afficher toutes les informations système :

```bash
./sysinfo.sh
```

Afficher uniquement les informations CPU :

```bash
./sysinfo.sh --cpu
```

Afficher uniquement la mémoire :

```bash
./sysinfo.sh --memory
```

Afficher uniquement l’espace disque :

```bash
./sysinfo.sh --disk
```

Afficher uniquement les informations réseau :

```bash
./sysinfo.sh --network
```

## Dépendances

* `uname`

* `lscpu`

* `free`

* `df`

* `ip` ou `ifconfig` selon les distributions

Ces commandes doivent être disponibles sur le système.

## Notes

* Le script ne modifie aucun paramètre du système, il est uniquement informatif.

* Certaines commandes peuvent nécessiter l’installation de paquets supplémentaires selon la distribution.

* Compatible avec toutes les distributions Linux.

* L’option `--all` est utilisée par défaut si aucune option n’est fournie.
