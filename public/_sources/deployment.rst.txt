====================================
🌐 Automatic Deployment
====================================

This page explains how documentation is deployed automatically.


How It Works
============

.. image:: https://img.shields.io/badge/GitHub-Actions-blue?logo=github
   :alt: GitHub Actions

When you ``git push`` to the ``main`` branch:

1. **GitHub Actions** detects the push
2. The ``.github/workflows/docs.yaml`` workflow runs
3. **uv** installs dependencies
4. **Sphinx** builds the documentation
5. HTML files are deployed to **GitHub Pages**
6. Documentation is live at https://simbouch.github.io/tutto_antony_2026_janvier/


Workflow File
=============

Contents of ``.github/workflows/docs.yaml``:

.. code-block:: yaml

   name: Deploy Documentation
   
   on:
     push:
       branches: [main]
   
   permissions:
     contents: write
     pages: write
     id-token: write
   
   jobs:
     build-docs:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v4
   
         - name: Install uv
           uses: astral-sh/setup-uv@v3
           with:
             version: "latest"
   
         - name: Install dependencies
           run: uv sync --all-extras
   
         - name: Build Sphinx Documentation
           run: uv run sphinx-build source public
   
         - name: Upload artifact
           uses: actions/upload-pages-artifact@v3
           with:
             path: 'public'
   
     deploy-docs:
       needs: build-docs
       runs-on: ubuntu-latest
       environment:
         name: github-pages
         url: ${{ steps.deployment.outputs.page_url }}
       steps:
         - name: Deploy to GitHub Pages
           id: deployment
           uses: actions/deploy-pages@v4


GitHub Pages Configuration
==========================

To enable automatic deployment:

1. Go to **Settings** → **Pages**
2. Set **Source**: ``GitHub Actions``
3. Save

That's it! Future pushes will deploy automatically.


Verify Deployment
=================

1. Go to GitHub → **Actions**
2. Find the "Deploy Documentation" workflow
3. Click to view logs
4. If green ✅ → visit https://simbouch.github.io/tutto_antony_2026_janvier/


Troubleshooting
===============

Error: "Pages not enabled"
--------------------------

- Go to Settings → Pages → Set GitHub Actions as source

Error: "Sphinx build failed"
----------------------------

- Verify ``source/index.rst`` exists
- Check ``source/conf.py``
- Test locally with ``uv run sphinx-build source public``

Error: "Permission denied"
--------------------------

Add these permissions to the workflow:

.. code-block:: yaml

   permissions:
     contents: write
     pages: write
     id-token: write


Documentation URL
=================

📖 **https://simbouch.github.io/tutto_antony_2026_janvier/**

