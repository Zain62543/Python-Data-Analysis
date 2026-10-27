# Logistic Regression: scikit-learn and From Scratch

Fits scikit-learn's logistic regression on the breast-cancer dataset with scaling and a train/test split, evaluates it with accuracy, confusion matrix and classification report, then re-implements logistic regression from scratch with gradient descent on a synthetic dataset (loss curve and decision boundary).

| | |
|---|---|
| **Notebook** | [`logistic-regression-breast-cancer.ipynb`](logistic-regression-breast-cancer.ipynb) |
| **Data** | scikit-learn `load_breast_cancer`, `make_classification` |
| **Techniques** | Logistic regression, gradient descent, evaluation metrics |
| **Libraries** | scikit-learn, NumPy, pandas, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/logistic-regression-breast-cancer/logistic-regression-breast-cancer.ipynb
```

- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
