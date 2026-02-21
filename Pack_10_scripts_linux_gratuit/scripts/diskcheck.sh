#!/bin/bash

# Vérifie l'espace disque et alerte si le seuil est dépassé

THRESHOLD=20
USAGE=$(df / | grep / | awk '{print $5}' | sed 's/%//')

echo "Espace disque utilisé : $USAGE%"

if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "Attention : espace disque faible."
else
    echo "Espace disque OK."
fi
