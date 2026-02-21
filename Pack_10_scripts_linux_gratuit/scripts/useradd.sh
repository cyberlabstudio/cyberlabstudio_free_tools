#!/bin/bash

# Crée un utilisateur + dossier + permissions

USER="$1"

if [ -z "$USER" ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

# Vérifie si l'utilisateur existe déjà
if id "$USER" &>/dev/null; then
    echo "Erreur : L'utilisateur $USER existe déjà."
    exit 1
fi

# Crée l'utilisateur
if sudo useradd -m "$USER"; then
    echo "Utilisateur $USER créé avec succès."
else
    echo "Erreur : Impossible de créer l'utilisateur $USER."
    exit 1
fi

# Définit le mot de passe
echo "Définissez le mot de passe pour $USER :"
sudo passwd "$USER"

if [ $? -eq 0 ]; then
    echo "Mot de passe défini avec succès pour $USER."
else
    echo "Erreur : Impossible de définir le mot de passe pour $USER."
    exit 1
fi
