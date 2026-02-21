#!/bin/bash

# Affiche CPU, RAM, uptime, kernel

echo "Informations système"
echo "------------------------"

# CPU
echo "CPU : $(lscpu | grep -i 'Nom de modèle' | awk -F ':' '{print $2}' | sed 's/^ *//')"

# RAM
echo "RAM : $(free -h | grep Mem | awk '{print $3 "/" $2}')"

# Uptime
echo "Uptime : $(uptime -p)"

# Kernel
echo "Kernel : $(uname -r)"
