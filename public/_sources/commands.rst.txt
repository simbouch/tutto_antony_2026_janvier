===================================
💻 Référence des Commandes
===================================

Toutes les commandes utiles pour ce projet.


🔧 Commandes uv
===============

Installation et environnement
-----------------------------

.. code-block:: bash

   # Installer uv
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Créer un nouveau projet
   uv init mon_projet
   
   # Synchroniser les dépendances (installe tout)
   uv sync
   
   # Synchroniser avec les extras (dev, docs)
   uv sync --all-extras

Ajouter/Supprimer des dépendances
---------------------------------

.. code-block:: bash

   # Ajouter une dépendance
   uv add requests
   
   # Ajouter une dépendance de dev
   uv add --dev pytest
   
   # Supprimer une dépendance
   uv remove requests

Exécuter des commandes
----------------------

.. code-block:: bash

   # Exécuter un script Python
   uv run python main.py
   
   # Exécuter pytest
   uv run pytest
   
   # Exécuter n'importe quelle commande
   uv run <commande>


🧪 Commandes pytest
===================

.. code-block:: bash

   # Lancer tous les tests
   uv run pytest
   
   # Tests avec plus de détails
   uv run pytest -v
   
   # Tests avec print() visible
   uv run pytest -s
   
   # Un fichier spécifique
   uv run pytest test/test_valid.py
   
   # Un test spécifique
   uv run pytest test/test_valid.py::test_true
   
   # Avec couverture de code
   uv run pytest --cov=.


📚 Commandes Sphinx
===================

.. code-block:: bash

   # Construire la documentation HTML
   uv run sphinx-build source public
   
   # Reconstruire tout (ignorer le cache)
   uv run sphinx-build -E source public
   
   # Mode verbose
   uv run sphinx-build -v source public


🐙 Commandes Git
================

.. code-block:: bash

   # Voir le statut
   git status
   
   # Ajouter tous les fichiers
   git add .
   
   # Créer un commit
   git commit -m "Message du commit"
   
   # Pousser vers GitHub
   git push
   
   # Récupérer les dernières modifications
   git pull
   
   # Voir l'historique
   git log --oneline


🔄 Commandes GitHub Actions
===========================

Pour déclencher manuellement le workflow (après un échec) :

.. code-block:: bash

   # Créer un commit vide pour déclencher le workflow
   git commit --allow-empty -m "Trigger workflow"
   git push

Ou va sur GitHub → Actions → Clique sur le workflow → "Re-run all jobs"

