# 📜 Script — `sysinfo.sh`
**CyberLabStudio • Pack 10 Scripts Linux Gratuits**

## 🧩 Description

Ce script affiche les informations essentielles du système en un seul coup d’œil.

Il permet de visualiser rapidement :

* La version du système

* L’état du CPU

* La mémoire utilisée et disponible

* L’espace disque

* Les informations réseau

* Le temps d’activité (uptime)

Idéal pour diagnostiquer un problème, vérifier l’état d’une machine ou générer un rapport système rapide.

## ⚙️ Fonctionnement

### Informations collectées

1. Version du système

```bash
lsb_release -a
```

2. Informations CPU

```bash
lscpu
```

3. Mémoire RAM

```bash
free -h
```

4. Espace disque

```bash
df -h
```

5. Adresse IP et interface réseau

```bash
ip a
```

6. Temps d’activité

```bash
uptime -p
```

### Format de sortie

Le script regroupe toutes ces informations dans un affichage clair et structuré, idéal pour une lecture rapide.

## 🧪 Exemples d’utilisation

### Afficher toutes les informations système :

```bash
./sysinfo.sh
```

### Exporter les informations dans un fichier :

```bash
./sysinfo.sh > rapport.txt
```

## 🚨 Notes et limitations

* **Compatibilité** : fonctionne sur toutes les distributions Linux

* **Dépendances** : nécessite `lsb_release` (paquet `lsb-release` sur certaines distros)

* **Permissions** : aucune permission spéciale requise

* **Variabilité** : certaines commandes peuvent varier selon la distribution

## 📌 Intégration avec d’autres scripts

* Utile avec `netcheck.sh` pour un diagnostic réseau complet

* Peut être utilisé avant `backup.sh` pour vérifier l’espace disque

* Idéal dans un workflow d’audit ou de maintenance système

## 🖤 CyberLabStudio © 2026

Packs publics • Outils & Apps • Scripts Linux • Templates Notion • Ressources techniques
