#!/bin/bash

# Synchronisation de deux dossiers

SOURCE="$1"
DEST="$2"

if [ -z "$SOURCE" ] || [ -z "$DEST" ]; then
	echo "Usage: ./sync.sh <source> <destination>"
	exit 1
fi

echo "Synchronisation de $SOURCE vers $DEST..."
rsync -avh --delete "$SOURCE" "$DEST"
echo "Synchronisation terminée."
