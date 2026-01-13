# 🚀 Tutto Antony 2026

[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue?logo=github)](https://simbouch.github.io/tutto_antony_2026_janvier/)
[![Python](https://img.shields.io/badge/python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/package%20manager-uv-blueviolet)](https://docs.astral.sh/uv/)
[![Sphinx](https://img.shields.io/badge/docs-Sphinx-orange?logo=sphinx)](https://www.sphinx-doc.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> **A modern Python project template** with automated documentation deployment using uv, Sphinx, and GitHub Actions.

## ✨ Features

- 📦 **Modern dependency management** with [uv](https://docs.astral.sh/uv/) (fast, reliable)
- 📚 **Beautiful documentation** with Sphinx + Read the Docs theme
- 🔄 **Automated deployment** via GitHub Actions to GitHub Pages
- ✅ **Testing** with pytest
- 🏗️ **Clean project structure** following Python best practices

## 📖 Documentation

**Live documentation**: [https://simbouch.github.io/tutto_antony_2026_janvier/](https://simbouch.github.io/tutto_antony_2026_janvier/)

The documentation includes:
- 🚀 Quick Start guide
- 💻 Command reference (uv, pytest, Sphinx, Git)
- 🌐 Deployment workflow explanation

## 🛠️ Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/simbouch/tutto_antony_2026_janvier.git
cd tutto_antony_2026_janvier

# Install dependencies (creates .venv automatically)
uv sync --all-extras
```

### Run Tests

```bash
uv run pytest
```

### Build Documentation Locally

```bash
uv run sphinx-build source public
# Open public/index.html in your browser
```

## 📁 Project Structure

```
tutto_antony_2026_janvier/
├── .github/workflows/docs.yaml   # GitHub Actions workflow
├── source/                       # Sphinx documentation source
│   ├── conf.py                   # Sphinx configuration
│   ├── index.rst                 # Documentation home
│   ├── quickstart.rst            # Getting started guide
│   ├── commands.rst              # Command reference
│   └── deployment.rst            # Deployment guide
├── test/test_valid.py            # Project tests
├── pyproject.toml                # Project configuration
├── uv.lock                       # Locked dependencies
└── main.py                       # Application entry point
```

## 🔄 How It Works

1. **Push to `main`** → triggers GitHub Actions
2. **uv** installs dependencies
3. **Sphinx** builds HTML documentation
4. **GitHub Pages** deploys automatically

## 🧪 Testing

```bash
uv run pytest      # Run all tests
uv run pytest -v   # Verbose output
```

## 📦 Tech Stack

| Tool | Purpose |
|------|---------|
| [uv](https://docs.astral.sh/uv/) | Package & environment management |
| [Sphinx](https://www.sphinx-doc.org/) | Documentation generator |
| [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/) | Read the Docs theme |
| [pytest](https://pytest.org/) | Testing framework |
| [GitHub Actions](https://github.com/features/actions) | CI/CD automation |

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

Made with ❤️ using modern Python tooling