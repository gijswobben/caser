from setuptools import find_packages, setup

with open("docs/README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# When installing, these requirements need to be satisfied
install_requirements: list[str] = []

# When installing for development, install these requirements
dev_requirements: list[str] = [
    "black>=22.3.0",
    "mypy>=0.950",
    "pytest~=7.1.2",
    "isort~=5.10.1",
    "pytest-cov~=3.0.0",
]

docs_requirements: list[str] = [
    "sphinx~=4.5.0",
    "myst-parser==0.17.2",
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
