==========================
🚀 Quickstart - Démarrage
==========================

Cette page explique comment démarrer avec ce projet.


1. Prérequis
============

Tu dois avoir **uv** installé sur ta machine.

.. code-block:: bash

   # Installer uv (Windows PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Vérifier que uv est installé
   uv --version


2. Cloner le projet
===================

.. code-block:: bash

   git clone https://github.com/simbouch/tutto_antony_2026_janvier.git
   cd tutto_antony_2026_janvier


3. Installer les dépendances
============================

.. code-block:: bash

   # uv crée automatiquement un environnement virtuel .venv
   uv sync --all-extras

Ce que fait ``uv sync`` :

- Lit ``pyproject.toml`` pour les dépendances
- Crée un ``.venv`` si besoin
- Installe toutes les dépendances (y compris dev/docs)
- Utilise ``uv.lock`` pour des versions reproductibles


4. Activer l'environnement (optionnel)
======================================

.. code-block:: bash

   # Windows PowerShell
   .\.venv\Scripts\Activate.ps1
   
   # Linux/Mac
   source .venv/bin/activate

.. note::
   Avec ``uv run``, tu n'as pas besoin d'activer manuellement !
   ``uv run <commande>`` utilise automatiquement le bon environnement.


5. Lancer les tests
===================

.. code-block:: bash

   uv run pytest

Tu devrais voir :

.. code-block:: text

   ========================= test session starts =========================
   collected 1 item
   
   test/test_valid.py .                                            [100%]
   
   ========================== 1 passed in 0.01s ==========================


6. Construire la documentation
==============================

.. code-block:: bash

   # Génère le HTML dans le dossier "public"
   uv run sphinx-build source public

Puis ouvre ``public/index.html`` dans ton navigateur.


7. Workflow quotidien
=====================

.. code-block:: bash

   # 1. Faire des modifications
   # 2. Tester
   uv run pytest
   
   # 3. Construire les docs pour vérifier
   uv run sphinx-build source public
   
   # 4. Commit et push
   git add .
   git commit -m "Description des changements"
   git push

Après le push, GitHub Actions déploie automatiquement les docs ! 🎉

