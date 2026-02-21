# 📜 Script — `sync.sh`
**CyberLabStudio • Pack 10 Scripts Linux Gratuits**

## 🧩 Description

Ce script permet de synchroniser deux dossiers en utilisant `rsync`, que ce soit en local ou vers un emplacement distant (SSH).

Il est idéal pour :

* Mettre à jour un dossier miroir

* Synchroniser des sauvegardes

* Répliquer des fichiers entre deux machines

* Automatiser des workflows de déploiement

## ⚙️ Fonctionnement

### Principe

Le script utilise `rsync` avec des options sécurisées pour synchroniser efficacement deux emplacements.

### Commande clé utilisée

```bash
rsync -avh --delete source/ destination/
```

### Modes supportés

* **Local → Local**

* **Local → Distant (SSH)**

* **Distant → Local (SSH)**

### Options utiles

* `--delete` : supprime les fichiers absents de la source

* `--progress` : affiche la progression

* `--dry-run` : simule la synchronisation sans rien modifier

## 🧪 Exemples d’utilisation

### Synchroniser deux dossiers locaux :

```bash
./sync.sh ~/Documents ~/Backup/Documents
```

### Synchroniser vers un serveur distant :

```bash
./sync.sh ~/projet user@serveur:/home/user/projet
```

### Simulation sans modification :

```bash
./sync.sh ~/source ~/destination --dry-run
```

## 🚨 Notes et limitations

* **Compatibilité** : fonctionne sur toutes les distributions Linux

* **Dépendance** : nécessite `rsync` (et `ssh` pour les synchronisations distantes)

* **Sécurité** : pour SSH, une clé privée est recommandée

* **Attention** : l’option `--delete` peut supprimer des fichiers non présents dans la source

## 📌 Intégration avec d’autres scripts

* Peut être utilisé après `backup.sh` pour synchroniser des sauvegardes

* Utile avec `diskcheck.sh` pour vérifier l’espace avant synchronisation

* Peut être intégré dans un workflow d’automatisation (cron, déploiement, réplication)

## 🖤 CyberLabStudio © 2026

Packs publics • Outils & Apps • Scripts Linux • Templates Notion • Ressources techniques
