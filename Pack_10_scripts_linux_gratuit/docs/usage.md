# 📘 Utilisation du Pack 10 Scripts Linux – CyberLabStudio
Ce document explique comment utiliser efficacement les 10 scripts Linux inclus dans le pack.
Chaque script est autonome, simple à exécuter et peut être personnalisé selon tes besoins.

## ▶️ 1. Exécuter un script

Une fois les permissions d’exécution ajoutées (voir installation.md), tu peux lancer n’importe quel script :

```bash
./nom_du_script.sh
```

## 🆘 2. Afficher l’aide d’un script

Chaque script inclut une option `--help` qui affiche :

- les options disponibles

- les paramètres

- un exemple d’utilisation

```bash
./nom_du_script.sh --help
```

## 📌 3. Description rapide des scripts

Voici un résumé des fonctionnalités principales :

 | Script       | Fonction principale                                                                                     |
 |--------------|---------------------------------------------------------------------------------------------------------|
 | `backup.sh`    | Sauvegarde un dossier avec timestamp |
 | `clean.sh`     | Nettoyage des fichiers temporaires et caches |
 | `compress.sh`  | Compression/décompression automatique |
 | `diskcheck.sh` | Vérification de l’espace disque |
 | `netcheck.sh`  | Tests réseau (ping, DNS, latence) |
 | `search.sh`    | Recherche de fichiers par nom ou contenu |
 | `sync.sh`      | Synchronisation de dossiers via rsync |
 | `sysinfo.sh`   | Informations système (CPU, RAM, kernel…) |
 | `update.sh`    | Mise à jour du système |
 | `useradd.sh`   | Création d’un utilisateur avec permissions |

Pour plus de détails, consulte les fiches individuelles dans `docs/`.

## 🔐 4. Scripts nécessitant sudo

Certains scripts doivent être exécutés avec des privilèges administrateur :

- `update.sh`

- `useradd.sh`

- `diskcheck.sh`

Exemple :

```bash
sudo ./update.sh
```

## 🧩 5. Personnaliser les scripts

Tous les scripts sont écrits en `bash` et peuvent être modifiés selon tes besoins.

Pour éditer un script :

```bash
nano nom_du_script.sh
```
ou

```bash
code nom_du_script.sh
```

Tu peux :

- changer les chemins

- modifier les options

- ajouter des logs

- automatiser via cron

## ⏱️ 6. Automatiser un script (cron)

Tu peux automatiser un script via `crontab`.

Exemple : exécuter `backup.sh` tous les jours à 2h du matin :

```bash
crontab -e
```

Puis ajouter :

```bash
0 2 * * * /chemin/vers/backup.sh
```

## 🧪 7. Tester un script avant utilisation

Pour éviter les erreurs, tu peux lancer un script en mode “test” (si disponible) :

```bash
./nom_du_script.sh --dry-run
```

Certains scripts incluent cette option, d’autres non.

## 📚 8. Documentation complémentaire

Tu trouveras dans le dossier `docs/` :

`installation.md`

`usage.md` (ce fichier)

`changelog.md`

fiches détaillées pour chaque script
