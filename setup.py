from setuptools import find_packages, setup
from typing import List

with open("docs/README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# When installing, these requirements need to be satisfied
install_requirements: List[str] = []

# When installing for development, install these requirements
dev_requirements: List[str] = [
    "black>=22.3.0",
    "mypy>=0.950",
    "pytest~=7.1.2",
    "isort~=5.10.1",
    "pytest-cov~=3.0.0",
]

docs_requirements: List[str] = [
    "sphinx~=4.5.0",
    "myst-parser==0.17.2",
    "sphinxcontrib-napoleon==0.7",
    "sphinx-material==0.0.35",
]

setup(
    name="caser",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gijs Wobben",
    url="",
    packages=find_packages(),
    python_requires=">3.7.0, <4.0.0",
    install_requires=install_requirements,
    extras_require={
        "dev": dev_requirements,
        "docs": docs_requirements,
    },
)
