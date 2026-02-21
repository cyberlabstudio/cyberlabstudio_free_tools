# 📜 Script — `backup.sh`
**CyberLabStudio • Pack 10 Scripts Linux Gratuits**

## 🧩 Description

Ce script permet de sauvegarder un dossier source vers un dossier de destination, en ajoutant automatiquement un **timestamp** pour conserver un historique clair et éviter les conflits.

Il est idéal pour :

* Sauvegarder régulièrement des documents

* Archiver des projets

* Automatiser des backups via cron

## ⚙️ Fonctionnement

### Principe

Le script utilise `rsync` pour effectuer une copie fiable et incrémentielle du dossier source vers un dossier de sauvegarde.

Chaque sauvegarde est stockée dans un sous-dossier nommé :

```bash
backup-YYYYMMDD-HHMMSS
```

### Commande clé utilisée

```bash
rsync -avh --progress /source/ /destination/backup-$(date +%Y%m%d-%H%M%S)/
```

## 🧪 Exemples d’utilisation

### Sauvegarder un dossier Documents :

```bash
./backup.sh ~/Documents ~/Backups
```

### Sauvegarder un projet vers un disque externe :

```bash
./backup.sh ~/projets /media/usb/backups
```

## 🚨 Notes et limitations

* **Compatibilité** : fonctionne sur toutes les distributions Linux

* **Dépendance** : nécessite `rsync`

* **Permissions** : assurez-vous d’avoir les droits d’écriture sur le dossier de destination

* **Espace disque** : les sauvegardes successives peuvent occuper beaucoup d’espace

## 📌 Intégration avec d’autres scripts

* Peut être combiné avec `compress.sh` pour créer des archives compressées

* Peut être utilisé avec `sync.sh` pour synchroniser des sauvegardes distantes

* Idéal dans un workflow d’automatisation (cron, scripts de maintenance, etc.)

## 🖤 CyberLabStudio © 2026

Packs publics • Outils & Apps • Scripts Linux • Templates Notion • Ressources techniques
