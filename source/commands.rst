===================================
💻 Command Reference
===================================

All useful commands for this project.


🔧 uv Commands
==============

Installation and Environment
----------------------------

.. code-block:: bash

   # Install uv
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Create a new project
   uv init my_project

   # Sync dependencies (install all)
   uv sync

   # Sync with extras (dev, docs)
   uv sync --all-extras

Add/Remove Dependencies
-----------------------

.. code-block:: bash

   # Add a dependency
   uv add requests

   # Add a dev dependency
   uv add --dev pytest

   # Remove a dependency
   uv remove requests

Execute Commands
----------------

.. code-block:: bash

   # Run a Python script
   uv run python main.py

   # Run pytest
   uv run pytest

   # Run any command
   uv run <command>


🧪 pytest Commands
==================

.. code-block:: bash

   # Run all tests
   uv run pytest

   # Verbose output
   uv run pytest -v

   # Show print() output
   uv run pytest -s

   # Specific file
   uv run pytest test/test_valid.py

   # Specific test
   uv run pytest test/test_valid.py::TestBasic::test_true

   # With code coverage
   uv run pytest --cov=.


📚 Sphinx Commands
==================

.. code-block:: bash

   # Build HTML documentation
   uv run sphinx-build source public

   # Rebuild all (ignore cache)
   uv run sphinx-build -E source public

   # Verbose mode
   uv run sphinx-build -v source public


🐙 Git Commands
===============

.. code-block:: bash

   # Check status
   git status

   # Add all files
   git add .

   # Create commit
   git commit -m "Commit message"

   # Push to GitHub
   git push

   # Pull latest changes
   git pull

   # View history
   git log --oneline


🔄 GitHub Actions Commands
==========================

To manually trigger the workflow (after a failure):

.. code-block:: bash

   # Create an empty commit to trigger workflow
   git commit --allow-empty -m "Trigger workflow"
   git push

Or go to GitHub → Actions → Click workflow → "Re-run all jobs"

