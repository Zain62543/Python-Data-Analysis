# Data Science & Machine Learning Notebooks

Hands-on notebooks covering Python, pandas and EDA, classical machine learning and deep learning, organised as **14 documented projects** plus a topic-grouped **learning archive**.

> **About this material.** These notebooks come from a structured data-science and AI training programme (May-August 2025). Most use standard teaching datasets such as Iris, breast cancer and CIFAR-10, so they show how I work through methods rather than client deliverables. For packaged, tested code, see [ML Classification Benchmark](https://github.com/Zain62543/Random-forest-classifiers-).

## Featured projects

Each project folder has a short README (data, techniques, libraries, how to run).

**Data wrangling & EDA**

| Project | What it shows | Data |
|---|---|---|
| [Netflix Catalogue: Data Cleaning Case Study](projects/netflix-data-cleaning/) | Missing values, parsing, feature derivation on a real catalogue | `data/netflix_titles_homework.csv` |
| [Air Quality: Missing-Data Analysis](projects/air-quality-missing-data/) | Missing-data visualisation, outliers, feature engineering | `data/air-quality.csv` |
| [Iris: EDA, PCA and K-Means](projects/eda-pca-kmeans-iris/) | Structured EDA, PCA, K-Means | scikit-learn `load_iris`, `make_blobs` |

**Supervised learning**

| Project | What it shows | Data |
|---|---|---|
| [Decision Trees on Iris](projects/decision-trees/) | Over/underfitting, feature importance, tuning | scikit-learn `load_iris` |
| [Logistic Regression: scikit-learn and From Scratch](projects/logistic-regression-breast-cancer/) | scikit-learn model plus a from-scratch implementation | scikit-learn `load_breast_cancer`, `make_classification` |
| [Regression and Classification Metrics](projects/regression-and-classification-metrics/) | MAE/RMSE/R², confusion-matrix metrics, ROC AUC | toy arrays for regression |
| [Cross-Validation and GridSearchCV](projects/cross-validation-and-grid-search/) | k-fold CV and GridSearchCV explained step by step | scikit-learn `load_breast_cancer` |
| [Bias, Variance and Over/Underfitting](projects/bias-variance-tradeoff/) | Bias, variance and ensembles | synthetic noisy cubic data |
| [Random Forests and Gradient Boosting](projects/random-forests-and-boosting/) | Bagging vs random forest vs gradient boosting | scikit-learn `load_breast_cancer` |

**Unsupervised learning**

| Project | What it shows | Data |
|---|---|---|
| [Hierarchical Clustering](projects/hierarchical-clustering/) | Linkage methods, dendrograms, PCA | scikit-learn `load_iris`, `make_blobs` |

**Deep learning**

| Project | What it shows | Data |
|---|---|---|
| [Road to Artificial Neural Networks](projects/ann-fundamentals/) | Logistic regression to softmax to perceptron (Keras) | scikit-learn `load_iris`, `load_wine`, `make_classification` |
| [Convolutional Neural Networks](projects/cnn-image-classification/) | CNNs on CIFAR-10 and Rock-Paper-Scissors | CIFAR-10 |
| [Hyperparameter Tuning with Keras Tuner](projects/keras-tuner-hyperparameter-search/) | Random-search tuning of ANN and CNN models | Fashion-MNIST and CIFAR-10 |
| [Transfer Learning: Feature Extraction and Fine-Tuning](projects/transfer-learning/) | VGG16 feature extraction, ResNet50 fine-tuning | `cats_and_dogs_filtered.zip` |

## Learning archive

`58` practice notebooks grouped by topic in [`learning-archive/`](learning-archive/): [python fundamentals](learning-archive/python-fundamentals/), [pandas and eda](learning-archive/pandas-and-eda/), [data collection](learning-archive/data-collection/), [classical machine learning](learning-archive/classical-ml/), [deep learning](learning-archive/deep-learning/), [llm apis](learning-archive/llm-apis/). These are working notes, and some cells are exploratory or unfinished.

## Repository layout

```text
.
├── projects/             # 14 documented projects: one folder, one notebook, one README each
├── learning-archive/     # 58 practice notebooks grouped by topic, numbered in learning order
├── data/                 # all shared datasets, referenced as ../../data/<file>
├── scripts/check_notebooks.py   # static notebook / data-path checker (also run in CI)
├── DATA.md               # every dataset: size, use, likely source, caveats
├── MIGRATION.md          # old path -> new path for every file
├── requirements.txt                 # core stack
├── requirements-deep-learning.txt   # TensorFlow, Keras Tuner, tensorflow-datasets
└── requirements-extras.txt          # scraping, SQL, PyTorch / Transformers, OpenAI
```

## Getting started

```bash
git clone https://github.com/Zain62543/Python-Data-Analysis.git
cd Python-Data-Analysis
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt                     # add the other requirements files as needed
jupyter lab
```

Open a notebook from its own folder; data paths are relative to it. Deep-learning notebooks need `requirements-deep-learning.txt` and are much faster on a GPU. API notebooks read keys from environment variables (`OPENAI_API_KEY`, `HF_API_KEY`); never paste keys into a notebook.

## Reliability notes

- Saved outputs are from the original runs. The notebooks were **not** re-executed after this reorganisation.
- `python scripts/check_notebooks.py` checks that every notebook is valid and that every local data file it references exists. It does not execute code.
- Library versions are not pinned, because the notebooks were written in 2025 and some APIs have since changed.

## Data and licence

Dataset sources and caveats are in [DATA.md](DATA.md). No licence has been chosen for this repository yet, so please contact me before reusing the notebooks, and check each dataset's own terms.

## Author

**Zain Ud Din** - MPhil Physics (Condensed Matter Physics) | Data Science, Machine Learning & Scientific Computing

[LinkedIn](https://www.linkedin.com/in/zain-ud-din-9152a2299/) · [GitHub profile](https://github.com/Zain62543)
