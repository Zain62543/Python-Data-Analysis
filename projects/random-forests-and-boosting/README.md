# Random Forests and Gradient Boosting

Contrasts bagging, random forests and gradient boosting and compares them on the breast-cancer data with repeated CV against a majority baseline and a single tree, impurity vs permutation importance, ROC curves, and boosting stages chosen on a validation split from the training data.

| | |
|---|---|
| **Notebook** | [`random-forest-vs-gradient-boosting-breast-cancer.ipynb`](random-forest-vs-gradient-boosting-breast-cancer.ipynb) |
| **Data** | scikit-learn `load_breast_cancer` |
| **Techniques** | Random forest, gradient boosting, ROC comparison |
| **Libraries** | scikit-learn, pandas, Seaborn, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/random-forests-and-boosting/random-forest-vs-gradient-boosting-breast-cancer.ipynb
```

- Methodology reviewed and revised; the notebook was **executed end-to-end** and the saved outputs come from that run (Python 3.13, scikit-learn 1.9, pandas 3.0).
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
