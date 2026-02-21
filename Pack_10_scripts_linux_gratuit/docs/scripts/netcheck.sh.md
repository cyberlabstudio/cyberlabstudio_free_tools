# 📄 FICHE TECHNIQUE — `netcheck.sh.md`

## Description

Ce script vérifie l’état de la connexion réseau et diagnostique les problèmes courants.

Il permet de :

* tester la connectivité Internet

* vérifier l’accès à une adresse ou un domaine spécifique

* mesurer le temps de réponse (ping)

* identifier rapidement une coupure réseau ou un problème DNS

Il simplifie le diagnostic réseau sur les systèmes Linux.

## Utilisation

```bash
./netcheck.sh [options]
```

## Options

| Option | Description |
|--------|-------------|
| `--host` | Teste la connectivité vers un hôte spécifique (ex : google.com) |
| `--ping` | Effectue un test de ping standard |
| `--dns` | Vérifie la résolution DNS |
| `--verbose` | Affiche des informations détaillées sur chaque étape |

## Exemples

Tester la connexion Internet par défaut :

```bash
./netcheck.sh
```

Tester la connectivité vers un domaine spécifique :

```bash
./netcheck.sh --host google.com
```

Effectuer un test de ping :

```bash
./netcheck.sh --ping
```

Vérifier la résolution DNS :

```bash
./netcheck.sh --dns
```

## Dépendances

* `ping`

* `dig` ou `nslookup` (selon les distributions)

* `curl` (selon les variantes du script)

Ces commandes doivent être disponibles sur le système.

## Notes

* Certaines commandes peuvent nécessiter `sudo` selon la configuration réseau.

* Le script utilise un hôte par défaut si aucun n’est spécifié (souvent `8.8.8.8` ou `google.com`).

* Compatible avec toutes les distributions Linux.

* Les résultats peuvent varier selon le pare-feu ou les règles réseau locales.
