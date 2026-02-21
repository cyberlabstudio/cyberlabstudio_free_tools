#!/bin/bash

# Recherche un fichier par nom ET/OU son contenu

QUERY="$1"
DIR="$2"

if [ -z "$QUERY" ] || [ -z "$DIR" ]; then
    echo "Usage: $0 <mot-clé> <dossier>"
    exit 1
fi

echo "Recherche de '$QUERY' dans '$DIR'..."

# Recherche de fichiers dont le nom CONTIENT le mot-clé
echo -e "\n=== Fichiers dont le nom contient '$QUERY' ==="
find "$DIR" -type f -name "*$QUERY*" 2>/dev/null

# Recherche de fichiers dont le CONTENU contient le mot-clé
echo -e "\n=== Contenu des fichiers contenant '$QUERY' ==="
grep -Rni --color=auto "$QUERY" "$DIR" 2>/dev/null

echo -e "\nRecherche terminée."
