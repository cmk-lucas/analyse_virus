# Détecteur de Virus et Scan Réseau

## Description
Ce projet est un logiciel de détection de virus et d'analyse réseau développé en Python. Il permet de scanner un système à la recherche de fichiers malveillants en les comparant à une base de signatures connues. Il inclut également une fonctionnalité de scan réseau pour détecter les machines actives.

## Fonctionnalités
- **Scan du système** : Analyse les fichiers dans des dossiers définis pour détecter des virus.
- **Scan réseau** : Permet de détecter les machines actives sur un réseau local.
- **Interface graphique** : Utilisation de Tkinter pour une navigation intuitive.
- **Génération de rapport** : Un fichier `virus_report.txt` est créé en cas de détection de fichiers infectés.

## Installation
### Prérequis
- Python 3.x
- Modules requis : `tkinter`

### Installation
1. Clonez ce dépôt :
   ```sh
   git clone https://github.com/cherubinmanunga/virus-scanner.git
   cd virus-scanner
   ```

# Exécution du script

```sh
python virus_scanner.py
```

# Utilisation

- **Scanner un système** : Cliquez sur "Lancer le scan système" pour analyser les fichiers.
- **Scanner un réseau** : Entrez une adresse IP de réseau et lancez l'analyse.
- **Ajouter un dossier personnalisé** : Ajoutez un dossier pour l'inclure dans l'analyse.

# Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus d’informations.

# Auteur

Développé par **Cherubin Manunga**.
