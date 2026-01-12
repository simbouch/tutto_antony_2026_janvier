========================================
🚀 Tutto Antony 2026 - Guide Complet
========================================

Bienvenue dans ce tutoriel ! Ce projet est un **exemple de référence** pour :

- ✅ Gérer un projet Python moderne avec **uv**
- ✅ Créer une documentation avec **Sphinx**
- ✅ Déployer automatiquement sur **GitHub Pages**
- ✅ Utiliser **GitHub Actions** pour le CI/CD

.. note::
   Ce guide est fait pour toi, Bouchaib ! Reviens ici quand tu as besoin d'un rappel.

.. toctree::
   :maxdepth: 2
   :caption: 📚 Sommaire

   quickstart
   commands
   deployment


🎯 C'est quoi ce projet ?
=========================

Ce projet montre comment :

1. **Initialiser** un projet Python avec ``uv``
2. **Écrire** de la documentation avec Sphinx
3. **Déployer** automatiquement sur GitHub Pages
4. **Tester** son code avec pytest

📁 Structure du Projet
======================

.. code-block:: text

   tutto_antony_2026_janvier/
   ├── .github/
   │   └── workflows/
   │       └── docs.yaml      # 🔄 GitHub Actions - déploie les docs
   ├── source/
   │   ├── conf.py            # ⚙️ Configuration Sphinx
   │   ├── index.rst          # 📄 Cette page !
   │   ├── quickstart.rst     # 🚀 Guide de démarrage
   │   ├── commands.rst       # 💻 Toutes les commandes
   │   └── deployment.rst     # 🌐 Comment ça se déploie
   ├── test/
   │   └── test_valid.py      # ✅ Tests pytest
   ├── pyproject.toml         # 📦 Config du projet Python
   ├── uv.lock                # 🔒 Versions exactes des deps
   └── main.py                # 🐍 Point d'entrée de l'app


⚡ Commandes Rapides
====================

Voici les commandes les plus utiles :

.. code-block:: bash

   # Installer les dépendances
   uv sync --all-extras

   # Lancer les tests
   uv run pytest

   # Construire la doc localement
   uv run sphinx-build source public

   # Voir la doc dans le navigateur
   # Ouvre public/index.html


🔗 Liens Utiles
===============

- `Documentation uv <https://docs.astral.sh/uv/>`_
- `Sphinx Documentation <https://www.sphinx-doc.org/>`_
- `GitHub Actions <https://docs.github.com/en/actions>`_
- `Read the Docs Theme <https://sphinx-rtd-theme.readthedocs.io/>`_

