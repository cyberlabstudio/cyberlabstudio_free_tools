<p align="center">
  <img src="assets/banner.png" alt="CyberLab Studio Banner" width="100%">
</p>

# Pack 10 Scripts Linux Gratuits - CyberLab Studio

![CyberLab Studio](https://img.shields.io/badge/CyberLab_Studio-Linux_Tools-6f42c1)
![Version](https://img.shields.io/github/v/release/cyberlabstudio/cyberlabstudio_free_tools)
![Downloads](https://img.shields.io/github/downloads/cyberlabstudio/cyberlabstudio_free_tools/v1.0.0/total)
![License](https://img.shields.io/github/license/cyberlabstudio/cyberlabstudio_free_tools)
![Status](https://img.shields.io/badge/maintenance-none-critical)
![Shell](https://img.shields.io/badge/scripts-bash-blue)

🔧 **10 scripts Linux prêts à l'emploi** pour automatiser vos tâches quotidiennes et optimiser votre productivité.

**Par CyberLab Studio** – Outils pour les passionnés de Linux et de sécurité informatique.

## 📥 Téléchargement

[Télécharger la dernière version (v1.0.0)](https://github.com/cyberlabstudio/cyberlabstudio_free_tools/releases/download/v1.0.0/CyberLabStudio_Linux_Script_Pack_v1.0.0.zip)

## 📌 Contenu du Pack

| Script | Description |
|--------|-------------|
| `backup.sh` | Sauvegarde un dossier source vers un dossier `backup` (avec timestamp). [Fiche détaillée](docs/scripts/backup.sh.md) |
| `clean.sh` | Nettoie les fichiers inutiles (cache, logs, fichiers temporaires) dans `/tmp` et `~/.cache`. [Fiche détaillée](docs/scripts/clean.sh.md) |
| `compress.sh` | Compresse/décompresse automatiquement des fichiers/dossiers (supporte `.zip`, `.tar.gz`). [Fiche détaillée](docs/scripts/compress.sh.md) |
| `diskcheck.sh` | Vérifie l'espace disque et envoie une alerte si le seuil critique (90%) est atteint. [Fiche détaillée](docs/scripts/diskcheck.sh.md) |
| `netcheck.sh` | Teste la connectivité réseau (ping, DNS, latence) et affiche un rapport. [Fiche détaillée](docs/scripts/netcheck.sh.md) |
| `search.sh` | Recherche un fichier par **nom** et/ou **contenu** (utilise `grep` et `find`). [Fiche détaillée](docs/scripts/search.sh.md) |
| `sync.sh` | Synchronise deux dossiers (utilise `rsync` pour une copie incrémentielle). [Fiche détaillée](docs/scripts/sync.sh.md) |
| `sysinfo.sh` | Affiche les infos système : CPU, RAM, uptime, version du kernel. [Fiche détaillée](docs/scripts/sysinfo.sh.md) |
| `update.sh` | Met à jour le système (compatible Debian/Ubuntu/Arch). [Fiche détaillée](docs/scripts/update.sh.md) |
| `useradd.sh` | Crée un utilisateur avec son dossier personnel et des permissions personnalisées. [Fiche détaillée](docs/scripts/useradd.sh.md) |

## 💡 Utilisation

Pour des instructions détaillées, consultez les **fiches Notion** incluses dans le pack (dossier `docs/`).

### 1. Donner les permissions d'exécution

```bash
chmod +x *.sh
```

### 2. Exécuter un script

```bash
./nom_du_script.sh --help  # Pour voir les options disponibles
```

## ⚠️ Prérequis

* **Système** : Linux (testé sur Ubuntu).

* **Dépendances** : `bash`, `grep`, `find`, `rsync`, `zip/unzip` (installés par défaut sur la plupart des distributions).

* **Permissions** : Certains scripts nécessitent des droits `sudo` (ex: `update.sh`, `useradd.sh`).

## 📁 Structure du dépôt

```bash
pack-10-scripts-linux/
│
├── scripts/          # Tous les scripts exécutables
├── docs/             # Documentation (installation, usage, changelog, fiches techniques)
├── notions/          # Fiches Notion (format marketing)
├── .gitignore
├── LICENSE           # Licence MIT
├── PACK.md           # Fiche du pack
├── README.md         # Documentation principale
├── SUPPORT.md        # Fichier support
├── SECURITY.md       # Fichier sécurité
└── VERSION.md        # Fichier version
```

## 📜 Licence

Ce pack est distribué sous licence MIT – libre d'utilisation, modification et partage.
Voir `LICENSE` pour plus de détails.

## 📬 Contact

💬 **Questions ou suggestions ?**

- Email : [CyberLabStudio@outlook.fr](mailto:CyberLabStudio@outlook.fr)

- Twitter : [@CyberLabStudio](https://twitter.com/CyberLabStudio)

- LinkedIn : [Jérôme Monico](https://www.linkedin.com/in/jerome-monico-b1ab0a37b)

---

**Merci d'utiliser nos outils !** ⭐ Si ce pack t'est utile, n'hésite pas à star ce dépôt sur GitHub.
