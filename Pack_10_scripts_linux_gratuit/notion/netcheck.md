# 📜 Script — `netcheck.sh`
**CyberLabStudio • Pack 10 Scripts Linux Gratuits**

## 🧩 Description

Ce script permet de tester rapidement l’état de la connexion réseau.
Il vérifie plusieurs éléments essentiels :

* Accessibilité d’Internet (ping)

* Résolution DNS

* Latence moyenne

* Disponibilité de la passerelle

Idéal pour diagnostiquer les problèmes réseau ou automatiser des tests de connectivité.

## ⚙️ Fonctionnement

### Tests effectués

1. Test de ping vers un serveur fiable (ex : 8.8.8.8)

```bash
ping -c 4 8.8.8.8
```

2. Test DNS via un nom de domaine

```bash
ping -c 4 google.com
```

3. Test de la passerelle locale

```bash
ip route | grep default
```

4. Mesure de la latence

Le script extrait automatiquement la latence moyenne depuis la sortie du ping.

## 🧪 Exemples d’utilisation

### Test complet de la connectivité :

```bash
./netcheck.sh
```

### Utilisation dans un script automatisé :

```bash
if ./netcheck.sh; then
    echo "Réseau OK"
else
    echo "Problème réseau détecté"
fi
```

## 🚨 Notes et limitations

* **Compatibilité** : fonctionne sur toutes les distributions Linux

* **Dépendances** : nécessite `ping` et `ip` (généralement installés par défaut)

* **Résultats** : la latence peut varier selon la charge réseau

* **DNS** : si le DNS échoue mais que le ping IP fonctionne, le problème vient du résolveur DNS

## 📌 Intégration avec d’autres scripts

* Peut être utilisé avant `update.sh` pour vérifier la connexion Internet

* Utile dans un workflow d’automatisation (scripts de monitoring, cron)

* Peut être combiné avec `sysinfo.sh` pour un diagnostic système complet

## 🖤 CyberLabStudio © 2026

Packs publics • Outils & Apps • Scripts Linux • Templates Notion • Ressources techniques
