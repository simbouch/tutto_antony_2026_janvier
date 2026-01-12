"""
Tests de validation pour le projet tutto_antony_2026_janvier.

Pour lancer les tests :
    uv run pytest
    uv run pytest -v   # mode verbose
"""

import os
from pathlib import Path


class TestProjectStructure:
    """Vérifie que la structure du projet est correcte."""

    def test_source_directory_exists(self):
        """Le dossier source/ doit exister."""
        assert Path("source").exists(), "Le dossier source/ n'existe pas"

    def test_conf_py_exists(self):
        """Le fichier conf.py doit exister."""
        assert Path("source/conf.py").exists(), "source/conf.py n'existe pas"

    def test_index_rst_exists(self):
        """Le fichier index.rst doit exister."""
        assert Path("source/index.rst").exists(), "source/index.rst n'existe pas"

    def test_pyproject_toml_exists(self):
        """Le fichier pyproject.toml doit exister."""
        assert Path("pyproject.toml").exists(), "pyproject.toml n'existe pas"

    def test_github_workflow_exists(self):
        """Le workflow GitHub Actions doit exister."""
        workflow = Path(".github/workflows/docs.yaml")
        assert workflow.exists(), ".github/workflows/docs.yaml n'existe pas"


class TestDocumentation:
    """Vérifie le contenu de la documentation."""

    def test_index_has_toctree(self):
        """index.rst doit contenir un toctree."""
        content = Path("source/index.rst").read_text(encoding="utf-8")
        assert "toctree" in content, "index.rst ne contient pas de toctree"

    def test_conf_has_rtd_theme(self):
        """conf.py doit utiliser le thème RTD."""
        content = Path("source/conf.py").read_text(encoding="utf-8")
        assert "sphinx_rtd_theme" in content, "Le thème RTD n'est pas configuré"

    def test_doc_pages_exist(self):
        """Les pages de documentation doivent exister."""
        pages = ["quickstart.rst", "commands.rst", "deployment.rst"]
        for page in pages:
            assert Path(f"source/{page}").exists(), f"source/{page} n'existe pas"


class TestBasic:
    """Tests basiques."""

    def test_true(self):
        """Test basique qui passe toujours."""
        assert True

    def test_python_version(self):
        """Python 3.10+ est requis."""
        import sys
        assert sys.version_info >= (3, 10), "Python 3.10+ requis"
