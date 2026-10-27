# Decision Trees on Iris

Trains a decision tree classifier, shows overfitting versus underfitting as depth changes, inspects feature importance, tunes hyperparameters with `GridSearchCV` and compares the result with logistic regression.

| | |
|---|---|
| **Notebook** | [`decision-trees.ipynb`](decision-trees.ipynb) |
| **Data** | scikit-learn `load_iris` |
| **Techniques** | Decision trees, tree plots, `GridSearchCV`, model comparison |
| **Libraries** | scikit-learn, pandas, Seaborn, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/decision-trees/decision-trees.ipynb
```

- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
