#!/bin/bash

# Vérifie la connectivité réseau

echo "Test de connexion..."
ping -c 3 google.com >/dev/null 2>&1

if [ $? -eq 0 ]; then
	echo "Internet OK."
else
	echo "Pas de connexion."
fi
