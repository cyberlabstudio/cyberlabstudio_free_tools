# 📄 FICHE TECHNIQUE — `search.sh.md`

## Description

Ce script recherche un mot-clé dans un ou plusieurs fichiers.

Il permet de :

* rechercher une chaîne de texte dans un fichier ou un dossier

* afficher les lignes correspondantes

* filtrer les résultats par extension

* effectuer une recherche récursive

Il simplifie la recherche de contenu dans les fichiers sur les systèmes Linux.

## Utilisation

```bash
./search.sh <mot_clé> <chemin> [options]
```

* `<mot_clé>` : texte à rechercher

* `<chemin>` : fichier ou dossier dans lequel effectuer la recherche

## Options

| Option | Description |
|--------|-------------|
| `--recursive` | Active la recherche récursive dans les sous-dossiers |
| `--ext` | Filtre les fichiers par extension (ex : `txt`, `log`, `sh`) |
| `--ignore-case` | Ignore la casse lors de la recherche |
| `--verbose` | Affiche les fichiers analysés |

## Exemples

Rechercher un mot dans un fichier :

```bash
./search.sh erreur /var/log/syslog
```

Rechercher un mot dans un dossier :

```bash
./search.sh TODO ~/projets
```

Recherche récursive :

```bash
./search.sh config /etc --recursive
```

Recherche dans les fichiers .log uniquement :

```bash
./search.sh fail /var/log --ext log
```

Recherche insensible à la casse :

```bash
./search.sh user ~/scripts --ignore-case
```

## Dépendances

* `grep`

* `find` (pour la recherche récursive)

Ces commandes sont disponibles par défaut sur toutes les distributions Linux.

## Notes

* Le script ne modifie aucun fichier, il est uniquement informatif.

* La recherche récursive peut être plus lente dans les dossiers volumineux.

* Compatible avec toutes les distributions Linux.

* L’option `--ext` ne fonctionne que si un dossier est fourni en second argument.
