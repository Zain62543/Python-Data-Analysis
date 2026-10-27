# Data Science & Machine Learning Notebooks

Hands-on notebooks covering Python, pandas and EDA, classical machine learning and deep learning, organised as **14 documented projects** plus a topic-grouped **learning archive**.

> **About this material.** These notebooks come from a structured data-science and AI training programme (May-August 2025). Most use standard teaching datasets such as Iris, breast cancer and CIFAR-10, so they show how I work through methods rather than client deliverables. For packaged, tested code, see [ML Classification Benchmark](https://github.com/Zain62543/Random-forest-classifiers-).

## Featured projects

Each project folder has a short README (data, techniques, libraries, how to run).

**Data wrangling & EDA**

| Project | What it shows | Data |
|---|---|---|
| [Netflix Catalogue: Data Cleaning Case Study](projects/netflix-data-cleaning/) | Documented missing-value policy, parsing, feature derivation with checks | `data/netflix_titles_homework.csv` |
| [Air Quality: Missing-Data Analysis](projects/air-quality-missing-data/) | Missingness diagnostics, imputation benchmarked by masking, outlier rules | `data/airQuality.csv` |
| [Iris: EDA, PCA and K-Means](projects/eda-pca-kmeans-iris/) | EDA, K-Means (elbow + silhouette), cluster validation, PCA | scikit-learn `load_iris`, `make_blobs` |

**Supervised learning**

| Project | What it shows | Data |
|---|---|---|
| [Decision Trees on Iris](projects/decision-trees/) | CV depth curve, permutation importance, tuning on train only | scikit-learn `load_iris` |
| [Logistic Regression: scikit-learn and From Scratch](projects/logistic-regression-breast-cancer/) | Leak-free evaluation plus a from-scratch gradient-descent model | scikit-learn `load_breast_cancer`, `make_classification` |
| [Regression and Classification Metrics](projects/regression-and-classification-metrics/) | MAE/RMSE/R², classification metrics, ROC AUC with bootstrap CI | toy arrays for regression |
| [Cross-Validation and GridSearchCV](projects/cross-validation-and-grid-search/) | Repeated CV, GridSearchCV, nested CV, final test once | scikit-learn `load_breast_cancer` |
| [Bias, Variance and Over/Underfitting](projects/bias-variance-tradeoff/) | Bias/variance by simulation, learning curves, bagging | synthetic noisy cubic data |
| [Random Forests and Gradient Boosting](projects/random-forests-and-boosting/) | Bagging vs random forest vs boosting with baselines and repeated CV | scikit-learn `load_breast_cancer` |

**Unsupervised learning**

| Project | What it shows | Data |
|---|---|---|
| [Hierarchical Clustering](projects/hierarchical-clustering/) | Linkage comparison, dendrograms, ARI / NMI validation | scikit-learn `load_iris`, `make_blobs` |

**Deep learning**

| Project | What it shows | Data |
|---|---|---|
| [Road to Artificial Neural Networks](projects/ann-fundamentals/) | Logistic regression to perceptron to a Keras neuron, with baselines | scikit-learn `load_iris`, `load_wine`, `make_classification` |
| [Convolutional Neural Networks](projects/cnn-image-classification/) | CNNs on CIFAR-10 and Rock-Paper-Scissors (revised, not re-run) | CIFAR-10 |
| [Hyperparameter Tuning with Keras Tuner](projects/keras-tuner-hyperparameter-search/) | Random-search tuning of ANN and CNN models (revised, not re-run) | Fashion-MNIST and CIFAR-10 |
| [Transfer Learning: Feature Extraction and Fine-Tuning](projects/transfer-learning/) | VGG16 feature extraction, two-stage ResNet50 fine-tuning (not yet run) | `cats_and_dogs_filtered.zip` |

## Learning archive

`59` practice notebooks grouped by topic in [`learning-archive/`](learning-archive/): [python fundamentals](learning-archive/python-fundamentals/), [pandas and eda](learning-archive/pandas-and-eda/), [data collection](learning-archive/data-collection/), [classical machine learning](learning-archive/classical-ml/), [deep learning](learning-archive/deep-learning/), [llm apis](learning-archive/llm-apis/). These are working notes, and some cells are exploratory or unfinished.

## Repository layout

```text
.
├── projects/             # 14 documented projects: one folder, one notebook, one README each
├── learning-archive/     # 59 practice notebooks grouped by topic, numbered in learning order
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

- **Projects:** the 14 notebooks in `projects/` were reviewed for methodology (leakage, baselines, honest evaluation). The 10 scikit-learn / pandas notebooks, and the scikit-learn cells of the ANN notebook, were re-executed and their outputs regenerated. The remaining TensorFlow cells (CNN, Keras Tuner, transfer learning, Keras part of ANN) were revised but could not be run in the environment used; their READMEs and in-notebook banners say exactly which outputs are stale or cleared. Run them once on a GPU runtime to regenerate.
- **Learning archive:** saved outputs are from the original runs and were not re-executed.
- `python scripts/check_notebooks.py` checks that every notebook is valid and that every local data file it references exists. It does not execute code.
- Library versions are not pinned, because the notebooks were written in 2025 and some APIs have since changed.

## Data and licence

Dataset sources and caveats are in [DATA.md](DATA.md). No licence has been chosen for this repository yet, so please contact me before reusing the notebooks, and check each dataset's own terms.

## Author

**Zain Ud Din** - MPhil Physics (Condensed Matter Physics) | Data Science, Machine Learning & Scientific Computing

[LinkedIn](https://www.linkedin.com/in/zain-ud-din-9152a2299/) · [GitHub profile](https://github.com/Zain62543)
