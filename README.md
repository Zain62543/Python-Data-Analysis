# Python, Data Analysis, and Machine Learning Practice

A portfolio of Jupyter notebooks and companion datasets, arranged mainly by course week and practice day. The collection follows a progression from Python fundamentals and data wrangling to classical machine learning, neural networks, and language model APIs. It also preserves the earlier Netflix exploratory analysis work already in this repository.

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
- `notebooks/` and `data/` — the existing focused Netflix EDA notebook and its companion dataset
- CSV, Excel, and SQLite files beside notebooks — companion data used in exercises

Start with the dated week folders for the learning sequence. The root-level notebooks include focused lessons such as cross-validation, machine learning pipelines, clustering, neural networks, and language model APIs. The earlier Netflix EDA is in `notebooks/RandomForest_Example.ipynb`.

## Getting started

1. Create and activate a Python environment with Jupyter Notebook or JupyterLab.
2. Install the core packages listed in `requirements.txt`. Some notebooks also use TensorFlow/Keras, Hugging Face Transformers, `openai`, or web-scraping packages.
3. Open a notebook and run its cells in order. Some notebooks expect a companion dataset at a relative path; launch Jupyter from the relevant notebook folder when needed.
4. API examples require your own provider account and credentials. Set credentials in environment variables, and never paste real keys into a notebook or commit them.

These are hands-on learning notes, so package versions and external APIs may change. Not every notebook is a standalone project or has been rerun in a clean environment.

## Data and attribution

Data files are included when they support an exercise. Dataset provenance and terms vary; check the original source and its license before reusing or redistributing any dataset. Some notebooks download data or call external services at runtime.

## Repository hygiene

Jupyter checkpoint folders, virtual document caches, local environment files, Anaconda's local project database, PDFs, generated presentations, and an unrelated dashboard workbook are excluded from version control. Notebook outputs are retained where present to preserve the original learning record.

## Author

**Zain Ud Din**

MPhil in Condensed Matter Theory | Computational Physics | Data Science and Machine Learning

- GitHub: [Zain62543](https://github.com/Zain62543)
- LinkedIn: [Zain Ud Din](https://www.linkedin.com/in/zain-ud-din-9152a2299/)
- Email: [marwatzain8@gmail.com](mailto:marwatzain8@gmail.com)

---

*Turning data and practice into useful insights.*
