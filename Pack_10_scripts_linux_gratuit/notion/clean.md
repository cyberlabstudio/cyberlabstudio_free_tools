# 📜 Script — `clean.sh`
**CyberLabStudio • Pack 10 Scripts Linux Gratuits**

## 🧩 Description

Ce script permet de nettoyer rapidement les fichiers temporaires et les caches inutiles du système.

Il supprime notamment :

* Les fichiers temporaires dans `/tmp`

* Les caches utilisateurs dans `~/.cache`

* Certains fichiers résiduels générés par des applications

Idéal pour libérer de l’espace disque et maintenir un système propre.

## ⚙️ Fonctionnement

### Zones nettoyées

* `/tmp` — fichiers temporaires système

* `~/.cache` — caches des applications utilisateur

* Fichiers temporaires divers selon la configuration

### Commandes clés utilisées

```bash
rm -rf /tmp/*
rm -rf ~/.cache/*
```

### Options avancées

* `--dry-run` : affiche ce qui serait supprimé sans exécuter

* `--verbose` : affiche les fichiers supprimés en détail

## 🧪 Exemples d’utilisation

### Nettoyage standard :

```bash
./clean.sh
```

### Nettoyage avec détails :

```bash
./clean.sh --verbose
```

### Simulation sans suppression :

```bash
./clean.sh --dry-run
```

## 🚨 Notes et limitations

* **Permissions** : certaines suppressions peuvent nécessiter `sudo`

* **Sécurité** : aucun fichier personnel n’est supprimé

* **Compatibilité** : fonctionne sur toutes les distributions Linux

* **Impact** : certaines applications peuvent recréer leurs caches au prochain lancement

## 📌 Intégration avec d’autres scripts

* Peut être utilisé avant `backup.sh` pour réduire la taille des sauvegardes

* Peut être intégré dans un workflow d’entretien automatisé (cron, maintenance hebdomadaire)

## 🖤 CyberLabStudio © 2026

Packs publics • Outils & Apps • Scripts Linux • Templates Notion • Ressources techniques
