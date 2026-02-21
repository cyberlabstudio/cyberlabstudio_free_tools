#!/bin/bash

# Compression ou décompression automatique

FILE="$1"

if [ -z "$FILE" ]; then
    echo "Usage: $0 <fichier_ou_dossier>"
    echo "Exemple : $0 mon_dossier/ ou $0 mon_fichier.txt"
    exit 1
fi

if [ ! -e "$FILE" ]; then
    echo "Erreur : '$FILE' n'existe pas."
    exit 1
fi

if [[ "$FILE" == *.tar.gz ]]; then
    echo "Décompression de '$FILE'..."
    if tar -xzf "$FILE"; then
        echo "Décompression terminée avec succès."
    else
        echo "Erreur lors de la décompression de '$FILE'."
        exit 1
    fi
else
    echo "Compression de '$FILE'..."
    if tar -czf "$FILE.tar.gz" "$FILE"; then
        echo "Compression terminée avec succès. Fichier créé : '$FILE.tar.gz'"
    else
        echo "Erreur lors de la compression de '$FILE'."
        exit 1
    fi
fi
