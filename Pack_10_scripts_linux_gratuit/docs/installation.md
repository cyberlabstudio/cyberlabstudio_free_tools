# 📦 Installation du Pack 10 Scripts Linux – CyberLabStudio
Ce guide explique comment installer et préparer les 10 scripts Linux inclus dans le pack.
Les étapes sont simples et compatibles avec toutes les distributions Linux courantes.

## 🗂️ 1. Télécharger le pack

Télécharge la dernière version du pack depuis la page GitHub Releases :

👉 [lien de téléchargement]

Tu obtiendras un fichier au format :

```bash
pack-10-scripts-linux-v1.0.zip
```

## 📁 2. Extraire l’archive

Dans ton terminal, place‑toi dans le dossier où se trouve le fichier `.zip`, puis exécute :

```bash
unzip pack-10-scripts-linux-v1.0.zip
```

Tu obtiendras une arborescence similaire à :

```bash
pack-10-scripts-linux/
│
├── scripts/
├── docs/
├── LICENSE
└── README.md
```

## 🔧 3. Donner les permissions d’exécution

Place‑toi dans le dossier `scripts/` :

```bash
cd pack-10-scripts-linux/scripts
```

Puis rends tous les scripts exécutables :

```bash
chmod +x *.sh
```

## ▶️ 4. Exécuter un script

Chaque script peut être lancé directement :

```bash
./nom_du_script.sh
```

Pour afficher les options disponibles :

```bash
./nom_du_script.sh --help
```

## ⚠️ 5. Scripts nécessitant des droits administrateur

Certains scripts demandent des privilèges `sudo`, par exemple :

- `update.sh`

- `useradd.sh`

- `diskcheck.sh` (selon la configuration)

Dans ce cas, exécute :

```bash
sudo ./nom_du_script.sh
```

## 🧩 6. Dépendances nécessaires

Les scripts utilisent uniquement des outils présents par défaut sur la majorité des distributions Linux :

- `bash`

- `grep`

- `find`

- `rsync`

- `zip` / `unzip`

- `df`, `du`, `top`, `uname`, etc.

Si une dépendance manque, installe‑la via ton gestionnaire de paquets :

**Debian / Ubuntu**

```bash
sudo apt install rsync zip unzip
```
**Arch Linux**

```bash
sudo pacman -S rsync zip unzip
```

## 🧪 7. Tester le bon fonctionnement

Tu peux tester rapidement :

```bash
./sysinfo.sh
./clean.sh
./netcheck.sh
```

Si ces scripts fonctionnent, tout le pack est opérationnel.

## 📚 8. Documentation complémentaire

Des fiches détaillées sont disponibles dans le dossier `docs/` :

- installation

- usage

- changelog

- fiches individuelles
