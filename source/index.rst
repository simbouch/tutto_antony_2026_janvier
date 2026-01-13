========================================
🚀 Tutto Antony 2026 - Documentation
========================================

A modern Python project template with automated documentation deployment.

.. image:: https://img.shields.io/badge/python-3.12+-blue?logo=python&logoColor=white
   :alt: Python 3.12+

.. image:: https://img.shields.io/badge/uv-package%20manager-blueviolet
   :alt: uv

.. image:: https://img.shields.io/badge/docs-Sphinx-orange?logo=sphinx
   :alt: Sphinx

----

✨ Features
===========

- 📦 **Modern dependency management** with `uv <https://docs.astral.sh/uv/>`_
- 📚 **Beautiful documentation** with Sphinx + Read the Docs theme
- 🔄 **Automated deployment** via GitHub Actions to GitHub Pages
- ✅ **Testing** with pytest
- 🏗️ **Clean project structure** following Python best practices

.. toctree::
   :maxdepth: 2
   :caption: 📚 Contents

   quickstart
   commands
   deployment


⚡ Quick Commands
=================

.. code-block:: bash

   # Install dependencies
   uv sync --all-extras

   # Run tests
   uv run pytest

   # Build documentation locally
   uv run sphinx-build source public


📁 Project Structure
====================

.. code-block:: text

   tutto_antony_2026_janvier/
   ├── .github/workflows/docs.yaml   # CI/CD workflow
   ├── source/                       # Documentation source
   │   ├── conf.py                   # Sphinx config
   │   ├── index.rst                 # This page
   │   ├── quickstart.rst            # Getting started
   │   ├── commands.rst              # Command reference
   │   └── deployment.rst            # Deployment guide
   ├── test/test_valid.py            # Tests
   ├── pyproject.toml                # Project config
   ├── uv.lock                       # Locked dependencies
   └── main.py                       # Entry point


🔗 Useful Links
===============

- `uv Documentation <https://docs.astral.sh/uv/>`_
- `Sphinx Documentation <https://www.sphinx-doc.org/>`_
- `GitHub Actions <https://docs.github.com/en/actions>`_
- `Read the Docs Theme <https://sphinx-rtd-theme.readthedocs.io/>`_
- `GitHub Repository <https://github.com/simbouch/tutto_antony_2026_janvier>`_

