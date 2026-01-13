==========================
🚀 Quick Start Guide
==========================

Get up and running with this project in minutes.


1. Prerequisites
================

**uv** must be installed on your machine.

.. code-block:: bash

   # Installer uv (Windows PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Vérifier que uv est installé
   uv --version


2. Clone the Project
====================

.. code-block:: bash

   git clone https://github.com/simbouch/tutto_antony_2026_janvier.git
   cd tutto_antony_2026_janvier


3. Install Dependencies
=======================

.. code-block:: bash

   # uv automatically creates a .venv virtual environment
   uv sync --all-extras

What ``uv sync`` does:

- Reads ``pyproject.toml`` for dependencies
- Creates ``.venv`` if needed
- Installs all dependencies (including dev/docs)
- Uses ``uv.lock`` for reproducible versions


4. Activate Environment (Optional)
==================================

.. code-block:: bash

   # Windows PowerShell
   .\.venv\Scripts\Activate.ps1

   # Linux/Mac
   source .venv/bin/activate

.. note::
   With ``uv run``, you don't need to activate manually!
   ``uv run <command>`` automatically uses the correct environment.


5. Run Tests
============

.. code-block:: bash

   uv run pytest

Expected output:

.. code-block:: text

   ========================= test session starts =========================
   collected 10 items

   test/test_valid.py ..........                                    [100%]

   ========================== 10 passed in 0.18s =========================


6. Build Documentation
======================

.. code-block:: bash

   # Generate HTML in the "public" folder
   uv run sphinx-build source public

Then open ``public/index.html`` in your browser.


7. Daily Workflow
=================

.. code-block:: bash

   # 1. Make changes
   # 2. Run tests
   uv run pytest

   # 3. Build docs to verify
   uv run sphinx-build source public

   # 4. Commit and push
   git add .
   git commit -m "Description of changes"
   git push

After push, GitHub Actions automatically deploys the docs! 🎉

