# Python data analysis project structure template

## Introduction

This is a suggested project setup for a data analysis project. It uses open source projects to help you streamline data analysis workflow, maintain a sane and sensible folder structure, and follow best practices. Specifically, it uses:
- [Poetry](https://python-poetry.org/) for environment and dependencies management
- [Nbdev](https://nbdev.fast.ai/) and [LineaPy](https://github.com/LineaLabs/lineapy) for seamless transitions from messy, exploratory Jupyter notebooks to reusable code and packages with beautiful documentation
- [Kedro](https://github.com/kedro-org/kedro) for datasource management via data catalogs and reproducible/visualizable pipelines
- [Prefect](https://www.prefect.io/) to orchestrate and schedule pipelines, with retries and complex error handling

... and other modern utility tools like linting with [ruff](https://github.com/charliermarsh/ruff), code coverage with [slipcover](https://github.com/plasma-umass/slipcover)

## Getting started

### Prerequisite

You need to have [Poetry](https://python-poetry.org/) installed globally and Python >=3.8,<3.11


```
.
├── conf
│   ├── base
│   ├── local
│   └── README.md
├── create-repository.py
├── data
│   ├── 01_raw
│   ├── 02_intermediate
│   ├── 03_primary
│   ├── 04_feature
│   ├── 05_model_input
│   ├── 06_models
│   ├── 07_model_output
│   └── 08_reporting
├── docs
│   └── source
├── kedro-answers.yml
├── LICENSE
├── logs
├── Makefile
├── MANIFEST.in
├── notebooks
│   ├── analyses
│   ├── exploratory
│   ├── generate_figures
│   └── package
├── poetry.lock
├── _proc
│   ├── 00_core.ipynb
│   ├── _docs
│   ├── index.ipynb
│   ├── nbdev.yml
│   ├── _quarto.yml
│   └── styles.css
├── _pyproject.toml
├── pyproject.toml
├── README_kedro.md
├── README.md
├── settings.ini
├── setup.py
└── src
    ├── requirements.txt
    ├── setup.py
    ├── test_package_project
    └── tests
```
