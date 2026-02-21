# 📄 FICHE TECHNIQUE — `diskcheck.sh.md`

## Description

Ce script vérifie l’espace disque disponible sur le système.

Il permet de :

* afficher l’espace utilisé et disponible sur chaque partition

* identifier rapidement les partitions proches de la saturation

* analyser l’espace occupé par les dossiers principaux

* aider au diagnostic avant une sauvegarde ou une installation

Il simplifie la surveillance de l’espace disque sur les systèmes Linux.

## Utilisation

```bash
./diskcheck.sh [options]
```

## Options

| Option | Description |
|--------|-------------|
| `--human` | Affiche les tailles dans un format lisible (équivalent à `df -h`) |
| `--details` | Affiche les dossiers les plus volumineux dans le répertoire courant |
| `--path` | Analyse un dossier spécifique pour afficher les tailles |

## Exemples

Afficher l’espace disque global :

```bash
./diskcheck.sh
```

Afficher l’espace disque dans un format lisible :

```bash
./diskcheck.sh --human
```

Afficher les dossiers les plus volumineux :

```bash
./diskcheck.sh --details
```

Analyser un dossier spécifique :

```bash
./diskcheck.sh --path /var/log
```

## Dépendances

* `df`

* `du`

Ces commandes sont disponibles par défaut sur toutes les distributions Linux.

## Notes

* Le script ne modifie aucun fichier, il est uniquement informatif.

* Certaines analyses détaillées peuvent nécessiter `sudo` selon les permissions.

* Compatible avec toutes les distributions Linux.

* L’option `--details` peut être plus lente sur les dossiers volumineux.
