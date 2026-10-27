# Regression and Classification Metrics

Computes MAE, MSE, RMSE and R-squared on small worked examples, then accuracy, precision, recall, F1 and ROC AUC; applies them to a breast-cancer classifier with a stratified split, a majority baseline and a bootstrap confidence interval for AUC.

| | |
|---|---|
| **Notebook** | [`regression-and-classification-metrics-roc-auc.ipynb`](regression-and-classification-metrics-roc-auc.ipynb) |
| **Data** | toy arrays for regression; scikit-learn `load_breast_cancer` for classification |
| **Techniques** | Regression metrics, classification metrics, ROC / AUC |
| **Libraries** | scikit-learn, Matplotlib, Seaborn |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/regression-and-classification-metrics/regression-and-classification-metrics-roc-auc.ipynb
```

- Methodology reviewed and revised; the notebook was **executed end-to-end** and the saved outputs come from that run (Python 3.13, scikit-learn 1.9, pandas 3.0).
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
