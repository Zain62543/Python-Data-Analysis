# Decision Trees on Iris

Trains a decision tree on Iris with a stratified split and a majority-class baseline, shows over-fitting with a cross-validated depth curve, compares impurity and permutation importance, tunes with `GridSearchCV` on the training data only, and compares against logistic regression with repeated CV and a single final test evaluation.

| | |
|---|---|
| **Notebook** | [`decision-tree-iris-overfitting-and-tuning.ipynb`](decision-tree-iris-overfitting-and-tuning.ipynb) |
| **Data** | scikit-learn `load_iris` |
| **Techniques** | Decision trees, tree plots, `GridSearchCV`, model comparison |
| **Libraries** | scikit-learn, pandas, Seaborn, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/decision-trees/decision-tree-iris-overfitting-and-tuning.ipynb
```

- Methodology reviewed and revised; the notebook was **executed end-to-end** and the saved outputs come from that run (Python 3.13, scikit-learn 1.9, pandas 3.0).
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
