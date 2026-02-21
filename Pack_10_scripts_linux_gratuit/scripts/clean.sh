#!/bin/bash

# Nettoyage des fichiers inutiles

echo "🧹 Nettoyage du système..."

if command -v apt >/dev/null 2>&1; then
    sudo apt autoremove -y
    sudo apt autoclean -y
elif command -v pacman >/dev/null 2>&1; then
    sudo pacman -Rns $(pacman -Qtdq) --noconfirm
fi

echo "✅ Nettoyage terminé."
