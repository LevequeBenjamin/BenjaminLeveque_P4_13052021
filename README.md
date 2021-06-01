# BenjaminLeveque_P4_13052021

## Développez un programme logiciel en Python

Le projet 4 de la formation Développeur d'application Python est un logiciel de tournoi géré selon le système de tournois "suisse" qui permet de gérer des événements hors ligne.

### Installation

Ce logiciel exécutable localement peut être installée en suivant les étapes décrites ci-dessous. L'usage de pipenv est recommandé.

1. Clonez le [repository](https://github.com/LevequeBenjamin/BenjaminLeveque_P4_13052021.git) à l'aide de la commande suivante :

`$ git clone "https://github.com/LevequeBenjamin/BenjaminLeveque_P4_13052021.git"` (vous pouvez également télécharger le code en temps [qu'archive zip](https://github.com/LevequeBenjamin/BenjaminLeveque_P4_13052021/archive/refs/heads/master.zip))

2. Exécutez l'application dans un environnement virtuel

Rendez-vous depuis un terminal à la racine du répertoire BenjaminLeveque_P4_13052021 avec la commande `$ cd BenjaminLeveque_P4_13052021`

Pour créez un environnement, utilisez la commande :

`$ python3 -m venv env` sous macos ou linux.

`$ python -m venv env` sous windows.

Pour activer l'environnement, exécutez la commande :

`$ source env/bin/activate` sous macos ou linux.

`$ env/Scripts/activate` sous windows.

3.  Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`

### Usage

Pour lancer le script utilisez la commande:

```

$ python chess_tournament.py

```

### Générer un rapport flake8

```

$ flake8 --format=html --htmldir=flake-report
```
