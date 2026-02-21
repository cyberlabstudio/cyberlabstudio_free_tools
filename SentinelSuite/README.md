# 🛡️ SentinelSuite Lite

> A lightweight toolkit for organizing labs, managing notes, and running optimized Nmap scans 🚀

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-0.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
![Issues](https://img.shields.io/github/issues/Dynamo76/SentinelSuiteLite)
![Stars](https://img.shields.io/github/stars/Dynamo76/SentinelSuiteLite?style=social)
![CI](https://github.com/Dynamo76/SentinelSuiteLite/actions/workflows/ci.yml/badge.svg?branch=main)
![CodeQL](https://github.com/Dynamo76/SentinelSuiteLite/actions/workflows/codeql.yml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/Dynamo76/SentinelSuiteLite/branch/main/graph/badge.svg)](https://codecov.io/gh/Dynamo76/SentinelSuiteLite)
[![Buy Me a Coffee](https://img.buymeacoffee.com/button-api/?text=Buy+me+a+coffee&emoji=☕&slug=Dynamo42&button_colour=5F7FFF&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00)](https://www.buymeacoffee.com/Dynamo42)


**SentinelSuite Lite** is a local assistant designed for CTF labs (TryHackMe, HackTheBox…).  
This free version (MVP) centralizes two essential modules to simplify pentest and training sessions.

---

## ✨ Main Features

### Modules: ###
- 🔍 **Scan Manager**: Nmap launcher with predefined profiles (Quick Analysis, Deep Analysis, etc.)
- 🗂 **Notes Manager**: lab notes in Markdown with templates (Linux, Web, Windows)
📁 Clear lab organization: notes, scans, reports, metadata
🕓 Automatic saving of scan results (`scan_history/`)
Modern interface built with **CustomTkinter**

---

## 📂 Project Structure
```
SentinelSuite/
├── assets/                 # Icons
├── core/
│   ├── __init__.py
│   ├── config_manager.py
│   ├── lab_manager.py      # Lab management
│   ├── nmap_launcher.py    # Nmap wrapper
│   └── notes_handler.py    # Markdown notes handler
├── gui/
│   ├── __init__.py
│   ├── history_viewer.py   # History GUI
│   ├── notes_manager.py    # Notes GUI 
│   ├── preferences.py      # Preferences GUI
│   └── scan_manager.py     # Nmap launcher GUI
├── labs/
│   ├── lab_001_tryhackme/
│   │   ├── metadata.json
│   │   ├── notes.md        # manual notes
│   │   ├── report.md       # premium version
│   │   └── scan.xml
│   ├── lab_002_hackthebox/
│   │   ├── metadata.json
│   │   ├── notes.md        # manual notes
│   │   ├── report.md       # premium version
│   │   └── scan.xml
│   └── templates/          # Note templates
│       ├── default.md
│       ├── linux.md
│       ├── web.md
│       └── windows.md
├── scan_history /          # Scan results
├── __init__.py
├── config.json
├── core_launcher.py        # Main interface
├── LICENSE.txt
├── README.md
└── Requirements.txt        # Dependencies
```
---

## ⚙️ Installation

1. Install **Python 3.10+**
2. Install **Nmap** and add it to PATH
3. Install dependencies :
   ```bash
   pip install customtkinter
4. Launch the application:
5. python core_launcher.py

---

## 🚀 Roadmap
### ✅ Version Lite (free)
- Scan Manager (Nmap + predefined profiles)
- Notes Manager (Markdown + templates)

---

### 💎 Premium Version (planned)

The Premium version of **SentinelSuite** will go far beyond the Lite MVP, offering advanced modules and features:

#### 📄 Reporting & Export
- **Report Generator**: automatic PDF/Markdown reports with screenshots and executed commands
- **Multi-format export**: PDF, HTML, Markdown for easy sharing
- **Cloud sync**: optional integration with GitHub/GitLab or cloud drives

#### 📊 Tracking & Statistics
- **Progress Tracker**: statistics, charts, and lab progression tracking
- **Enhanced History Viewer**: filters, search, detailed timeline

#### 👤 User & Training
- **User Profiles**: preferences, history, themes, multi-user support
- **Instructor Mode**: designed for trainers to manage labs with multiple participants simultaneously
- **Shared labs**: collaborative lab sessions with shared notes and scans
- **Role management**: distinction between instructor and student profiles

#### 🤖 Smart Assistance
- **Smart Assistant**: command suggestions, external resources, contextual help
- **AI Notes Assistant**: auto-completion of notes with contextual hints
- **AI Report Enhancer**: enrich reports with recommendations and learning resources

#### ⚙️ Scan Management
- **Advanced Scan Manager**: Aggressive/custom profiles, stealth scans (Null, Xmas, FIN, ACK)
- **Scheduled scans**: automated recurring scans
- **CVE integration**: mapping detected services with vulnerability databases (CVE, Vulners API)

#### 🎨 Customization
- **Settings & Localization**: advanced themes, dark/light mode, fr/en translation
- **Custom themes**: cyberpunk, minimal, or user-defined
- **Dashboard overview**: interactive graphs and summaries of labs and scans

---

### 📊 Lite vs Premium at a glance

| Feature / Module        | Lite (MVP) 🚀 | Premium (planned) 💎 |
|--------------------------|---------------|---------------------|
| **Scan Manager**         | Quick, Full, Stealth, UDP profiles | Aggressive/custom profiles, stealth scans, scheduled scans |
| **Notes Manager**        | Markdown notes + templates | Dynamic templates, AI-assisted notes |
| **Labs**                 | Organization (notes, scans, metadata) | Shared labs, Instructor Mode, role management |
| **History Viewer**       | Simple logs | Filters, search, detailed timeline |
| **Preferences**          | Theme, language, UI mode | User Profiles (multi-user, history, themes) |
| **Report Generator**     | — | PDF/Markdown enriched with screenshots and commands |
| **Progress Tracker**     | — | Statistics, charts, lab progression |
| **Instructor Mode**      | — | Multi-user sessions, collaborative labs, role management for trainers/students |
| **Smart Assistant**      | — | Command suggestions, AI notes/report enhancer |
| **Settings & Localization** | Basic | Advanced themes, fr/en translation |
| **Integration**          | — | Cloud sync, CVE mapping, API/CLI mode |

---

## 📣 Feedback
Your feedback is essential to improve SentinelSuite Lite.
- Open an **issue** on GitHub
- Join the **discussions**
- Share your opinion on module usefulness and your needs

---

## 👥 Contributeurs

Merci à toutes les personnes qui contribuent à ce projet 💖  

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

---

## 💖 Support
If you like SentinelSuite Lite and would like to support its development, feel free to buy me a coffee.

---

## 📜 Licence
Open-source project under the MIT License.

---
