#!/bin/bash

# Sauvegarde d'un dossier vers un dossier backup

SOURCE="$1"
DEST="$2"

if [ -z "$SOURCE" ] || [ -z "$DEST" ]; then
    echo "Usage: ./backup.sh <source> <destination>"
    exit 1
fi

echo "📦 Sauvegarde de $SOURCE vers $DEST..."
rsync -avh --progress "$SOURCE" "$DEST"
echo "✅ Sauvegarde terminée."
