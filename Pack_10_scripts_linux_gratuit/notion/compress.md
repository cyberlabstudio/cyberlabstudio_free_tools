# 📜 Script — `compress.sh`
**CyberLabStudio • Pack 10 Scripts Linux Gratuits**

## 🧩 Description

Ce script permet de compresser ou extraire des archives de manière simple et intuitive. Il supporte les formats suivants :

* `.tar.gz` (compression/décompression avec `tar`.

* `.zip` (compression/décompression avec `zip`/`unzip`.

Idéal pour sauvegarder des dossiers, transférer des fichiers ou libérer de l’espace disque.

## ⚙️ Fonctionnement

### Commandes clés utilisées

#### Compression en `.tar.gz`

```bash
tar -czvf archive.tar.gz /dossier/
```

#### Décompression d'un `.tar.gz`

```bash
tar -xzvf archive.tar.gz
```

#### Compression en `.zip`

```bash
zip -r archive.zip /dossier/
```

#### Décompression d'un `.zip`

```bash
unzip archive.zip
```

### Options utiles

Lister le contenu d’une archive :

```bash
tar -tf archive.tar.gz`
```

## 🧪 Exemples d’utilisation

### Compresser un dossier :

```bash
./compress.sh --compress dossier/
```

### Décompresser une archive :

```bash
./compress.sh --extract archive.tar.gz
```

### Compresser en .zip :

```bash
./compress.sh --zip dossier/
```

## 🚨 Notes et limitations

* **Compatibilité** : Fonctionne sur tous les systèmes Linux/Unix (nécessite `tar`, `zip`, et `unzip`).

* **Permissions** : Assurez-vous d’avoir les droits en écriture sur le dossier de destination.

* **Espace disque** : Vérifiez l’espace disponible avant de compresser de gros dossiers.

## 📌 Intégration avec d’autres scripts

* Peut être combiné avec `backup.sh` pour sauvegarder les dossiers compressés.

* Utilisable dans un workflow d’automatisation (ex: sauvegardes planifiées).

## 🖤 CyberLabStudio © 2026

Packs publics • Outils & Apps • Scripts Linux • Templates Notion • Ressources techniques
