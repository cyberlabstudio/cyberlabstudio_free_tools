# 📜 Script — `update.sh`
**CyberLabStudio • Pack 10 Scripts Linux Gratuits**

## 🧩 Description

Ce script permet de mettre à jour rapidement le système Linux, en effectuant :

* La mise à jour de la liste des paquets

* L’installation des mises à jour disponibles

* Le nettoyage des paquets obsolètes

Il est idéal pour maintenir un système à jour, sécurisé et performant.

## ⚙️ Fonctionnement

### Commandes clés utilisées

1. Mise à jour de la liste des paquets

```bash
sudo apt update
```

2. Installation des mises à jour

```bash
sudo apt upgrade -y
```

3. Nettoyage des paquets inutiles

```bash
sudo apt autoremove -y
sudo apt autoclean
```

### Options utiles

* `--full` : effectue une mise à niveau complète (`full-upgrade`)

* `--dry-run` : simule les mises à jour sans rien installer

## 🧪 Exemples d’utilisation


### Mise à jour standard :

```bash
./update.sh
```

### Mise à jour complète :

```bash
./update.sh --full
```

### Simulation sans installation :

```bash
./update.sh --dry-run
```

## 🚨 Notes et limitations

* **Compatibilité** : conçu pour les systèmes basés sur Debian/Ubuntu

* **Permissions** : nécessite `sudo`

* **Risque** : certaines mises à jour majeures peuvent nécessiter un redémarrage

* **Dépendances** : utilise `apt`, non compatible Arch/Fedora

## 📌 Intégration avec d’autres scripts

* Peut être utilisé avant `netcheck.sh` pour vérifier la connexion réseau

* Idéal dans un workflow de maintenance automatisée (cron)

* Peut être combiné avec `clean.sh` pour optimiser l’espace après mise à jour

## 🖤 CyberLabStudio © 2026

Packs publics • Outils & Apps • Scripts Linux • Templates Notion • Ressources techniques
