# 📜 Script — `diskcheck.sh`
**CyberLabStudio • Pack 10 Scripts Linux Gratuits**

## 🧩 Description

Ce script analyse l’espace disque disponible et alerte l’utilisateur lorsque un seuil critique est atteint (par défaut : **90% d’utilisation**).

Il est idéal pour :

* Surveiller l’état du stockage

* Prévenir les saturations de disque

* Automatiser des alertes système

## ⚙️ Fonctionnement

### Principe

Le script utilise la commande `df` pour analyser l’espace disque et détecter les partitions proches de la saturation.

### Commande clé utilisée

```bash
df -h
```

Le script compare ensuite le pourcentage d’utilisation avec un seuil configurable.

### Option principale
* `--threshold X` : définit un seuil personnalisé (ex : `--threshold 85`)

## 🧪 Exemples d’utilisation

### Analyse standard :

```bash
./diskcheck.sh
```

### Analyse avec seuil personnalisé :

```bash
./diskcheck.sh --threshold 80
```

## 🚨 Notes et limitations

* **Compatibilité** : fonctionne sur toutes les distributions Linux

* **Permissions** : certaines partitions peuvent nécessiter `sudo`

* **Seuil par défaut** : 90% d’utilisation

* **Alertes** : affichées directement dans le terminal

## 📌 Intégration avec d’autres scripts

* Peut être utilisé avant `backup.sh` pour vérifier l’espace disponible

* Peut être intégré dans un workflow d’automatisation (cron, maintenance système)

* Utile en complément de `clean.sh` pour libérer de l’espace en cas d’alerte

## 🖤 CyberLabStudio © 2026

Packs publics • Outils & Apps • Scripts Linux • Templates Notion • Ressources techniques
