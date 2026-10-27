# Python, Data Analysis, and Machine Learning Practice

A learning portfolio of Jupyter notebooks and companion datasets, arranged mainly by course week and practice day. The collection follows a progression from Python fundamentals and data wrangling to classical machine learning, neural networks, and language model APIs.

## Learning topics

- Python fundamentals, functions, object-oriented programming, and data structures
- NumPy, pandas, data cleaning, missing values, and exploratory data analysis
- Visualization, APIs, and introductory web scraping
- Regression, logistic regression, decision trees, random forests, model evaluation, and cross-validation
- PCA, t-SNE, clustering, and bias-variance concepts
- Artificial neural networks, CNNs, RNNs, transfer learning, and text generation
- Example integrations with OpenAI and Hugging Face APIs

## Repository layout

- `week1-12-may` through `week10-12-july` — dated practice notebooks, generally grouped by week and day
- `Home_work_Netflix` — an exploratory analysis case study and its dataset
- `Practice_navttc_exam` — Python and OOP practice
- Root-level notebooks — selected machine learning lessons and later deep learning/API exercises
- CSV files beside notebooks — companion datasets used in exercises

Start with the dated week folders for the learning sequence. The root-level notebooks include focused lessons such as cross-validation, machine learning pipelines, clustering, neural networks, and language model APIs.

## Getting started

1. Create and activate a Python environment with Jupyter Notebook or JupyterLab.
2. Install the packages needed by the notebook you want to run. Common packages include `numpy`, `pandas`, `matplotlib`, `seaborn`, and `scikit-learn`. Some notebooks also use TensorFlow/Keras, Hugging Face Transformers, `openai`, or web-scraping packages.
3. Open a notebook and run its cells in order. Some notebooks expect a companion CSV to be available at the relative path used in the notebook; launching Jupyter from this repository usually keeps those paths straightforward.
4. API examples require your own provider account and credentials. Set credentials in environment variables, and never paste real keys into a notebook or commit them.

These are hands-on learning notes, so package versions and external APIs may change. Not every notebook is a standalone project or has been rerun in a clean environment.

## Data and attribution

CSV files are included when they support an exercise. Dataset provenance and terms vary; check the original source and its license before reusing or redistributing any dataset. Some notebooks download data or call external services at runtime.

## Repository hygiene

Jupyter checkpoint folders, virtual document caches, local environment files, and Python cache files are excluded from version control. Notebook outputs are retained where present to preserve the original learning record.
