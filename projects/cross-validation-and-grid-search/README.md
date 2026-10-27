# Cross-Validation and GridSearchCV

Holds out a stratified test set first, then does all cross-validation and tuning on the training data: repeated CV with a baseline, scaling inside pipelines, `GridSearchCV` for a tree and a logistic regression, nested CV to measure how optimistic `best_score_` is, and one final test evaluation.

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

- Methodology reviewed and revised; the notebook was **executed end-to-end** and the saved outputs come from that run (Python 3.13, scikit-learn 1.9, pandas 3.0).
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
