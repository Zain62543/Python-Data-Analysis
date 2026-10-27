# Logistic Regression: scikit-learn and From Scratch

Fits a scikit-learn logistic regression on the breast-cancer data (stratified split, scaler inside a pipeline, majority baseline, cross-validated accuracy / recall / ROC-AUC), then re-implements logistic regression from scratch with gradient descent on a held-out toy dataset and checks it against scikit-learn without regularisation.

| | |
|---|---|
| **Notebook** | [`logistic-regression-sklearn-and-from-scratch.ipynb`](logistic-regression-sklearn-and-from-scratch.ipynb) |
| **Data** | scikit-learn `load_breast_cancer`, `make_classification` |
| **Techniques** | Logistic regression, gradient descent, evaluation metrics |
| **Libraries** | scikit-learn, NumPy, pandas, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/logistic-regression-breast-cancer/logistic-regression-sklearn-and-from-scratch.ipynb
```

- Methodology reviewed and revised; the notebook was **executed end-to-end** and the saved outputs come from that run (Python 3.13, scikit-learn 1.9, pandas 3.0).
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
