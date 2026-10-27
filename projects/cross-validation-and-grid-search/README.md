# Cross-Validation and GridSearchCV

Runs 5-fold cross-validation for logistic regression and a decision tree, then explains step by step how `GridSearchCV` searches hyperparameters and how to read `best_params_` and `best_score_`, finishing with test-set performance of the tuned tree.

| | |
|---|---|
| **Notebook** | [`cross-validation-and-gridsearch-breast-cancer.ipynb`](cross-validation-and-gridsearch-breast-cancer.ipynb) |
| **Data** | scikit-learn `load_breast_cancer` |
| **Techniques** | k-fold cross-validation, hyperparameter search |
| **Libraries** | scikit-learn, pandas, Seaborn, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/cross-validation-and-grid-search/cross-validation-and-gridsearch-breast-cancer.ipynb
```

- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
