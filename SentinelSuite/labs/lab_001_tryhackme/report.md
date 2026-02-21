# 🧾 Rapport – Green (TryHackMe)

## Résumé
Scan effectué sur 10.10.10.40 – OS Windows – Ports ouverts : 445, 139

## Commandes utilisées
- `nmap -sS -sV -O 10.10.10.40`

## Résultats
- SMB vulnérable à EternalBlue
- Accès root obtenu via Metasploit

## Flags
- user.txt : THM{abc123}
- root.txt : THM{def456}
