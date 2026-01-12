====================================
🌐 Déploiement Automatique
====================================

Cette page explique comment les docs sont déployées automatiquement.


Comment ça marche ?
===================

.. image:: https://img.shields.io/badge/GitHub-Actions-blue?logo=github
   :alt: GitHub Actions

Quand tu fais ``git push`` sur la branche ``main`` :

1. **GitHub Actions** détecte le push
2. Le workflow ``.github/workflows/docs.yaml`` se lance
3. **uv** installe les dépendances
4. **Sphinx** construit la documentation
5. Les fichiers HTML sont déployés sur **GitHub Pages**
6. Ta doc est visible sur https://simbouch.github.io/tutto_antony_2026_janvier/


Le fichier workflow
===================

Voici le contenu de ``.github/workflows/docs.yaml`` :

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


Configuration GitHub Pages
==========================

Pour que ça marche, il faut activer GitHub Pages :

1. Va dans **Settings** → **Pages**
2. Choisis **Source** : ``GitHub Actions``
3. Sauvegarde

C'est tout ! Les prochains push déploieront automatiquement.


Vérifier le déploiement
=======================

1. Va sur GitHub → **Actions**
2. Tu vois le workflow "Deploy Documentation"
3. Clique dessus pour voir les logs
4. Si c'est vert ✅ → va sur https://simbouch.github.io/tutto_antony_2026_janvier/


Résoudre les problèmes
======================

Erreur "Pages not enabled"
--------------------------

- Va dans Settings → Pages → Active GitHub Actions comme source

Erreur "Sphinx build failed"
----------------------------

- Vérifie que ``source/index.rst`` existe
- Vérifie ``source/conf.py``
- Teste localement avec ``uv run sphinx-build source public``

Erreur "Permission denied"
--------------------------

Ajoute ces permissions dans le workflow :

.. code-block:: yaml

   permissions:
     contents: write
     pages: write
     id-token: write


URL de ta documentation
=======================

📖 **https://simbouch.github.io/tutto_antony_2026_janvier/**

Garde ce lien en favoris !

