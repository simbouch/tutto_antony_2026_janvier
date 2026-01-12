# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'Tutto Antony 2026'
copyright = '2026, Bouchaib'
author = 'Bouchaib'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      # Auto-generate docs from docstrings
    'sphinx.ext.viewcode',     # Add links to source code
    'sphinx.ext.napoleon',     # Support Google/NumPy docstrings
]

templates_path = ['_templates']
exclude_patterns = []

# Language
language = 'fr'

# -- Options for HTML output -------------------------------------------------
# Use the Read the Docs theme (much nicer!)
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'style_nav_header_background': '#2980B9',
}

html_static_path = ['_static']

# Logo and branding (optional - create these files if you want)
# html_logo = '_static/logo.png'
# html_favicon = '_static/favicon.ico'
