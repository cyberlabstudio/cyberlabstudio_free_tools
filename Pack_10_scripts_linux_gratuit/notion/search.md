# 📜 Script — `search.sh`
**CyberLabStudio • Pack 10 Scripts Linux Gratuits**

## 🧩 Description

Ce script permet de rechercher un fichier par **nom** et/ou par **contenu**, en utilisant les commandes Linux `find` et `grep`.

Il est idéal pour :

* Retrouver rapidement un fichier perdu

* Chercher un mot-clé dans plusieurs fichiers

* Auditer un dossier ou un projet

* Diagnostiquer des erreurs dans des logs

## ⚙️ Fonctionnement

### Modes de recherche

1. Recherche par nom

```bash
find /chemin -type f -name "motif"
```

2. Recherche par contenu

```bash
grep -R "mot clé" /chemin
```

3. Recherche combinée

Le script peut combiner les deux méthodes pour affiner les résultats.

### Options principales

* `-n` : recherche par nom

* `-c` : recherche par contenu

* `-p` : chemin de recherche (par défaut : dossier courant)

## 🧪 Exemples d’utilisation

### Rechercher un fichier nommé `config.txt` :

```bash
./search.sh -n config.txt
```

### Rechercher un mot-clé dans tous les fichiers du dossier `/etc` :

```bash
./search.sh -c "password" -p /etc
```

### Rechercher un fichier contenant un mot-clé :

```bash
./search.sh -n "*.log" -c "error"
```

## 🚨 Notes et limitations

* **Compatibilité** : fonctionne sur toutes les distributions Linux

* **Performance** : la recherche peut être longue sur de gros dossiers

* **Permissions** : certains dossiers nécessitent `sudo`

* **Sensibilité à la casse** : dépend des options `grep` (modifiable dans le script)

## 📌 Intégration avec d’autres scripts

* Peut être utilisé avec `sysinfo.sh` pour diagnostiquer des erreurs système

* Utile avant `backup.sh` pour identifier les fichiers importants

* Peut être intégré dans un workflow d’audit ou de maintenance

## 🖤 CyberLabStudio © 2026

Packs publics • Outils & Apps • Scripts Linux • Templates Notion • Ressources techniques
