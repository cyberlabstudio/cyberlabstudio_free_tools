#!/bin/bash

# Script de mise à jour du système (Debian/Ubuntu/Arch) 

echo "🔄 Mise à jour du système..." 

if command -v apt >/dev/null 2>&1; then 
	sudo apt update && sudo apt upgrade -y 
elif command -v pacman >/dev/null 2>&1; then 
	sudo pacman -Syu --noconfirm 
else 
	echo "❌ Gestionnaire de paquets non reconnu." 
fi 

echo "✅ Mise à jour terminée."
