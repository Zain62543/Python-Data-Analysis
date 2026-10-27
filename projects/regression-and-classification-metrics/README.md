# Regression and Classification Metrics

Computes MAE, MSE, RMSE and R-squared on small worked regression examples, then the main classification metrics (accuracy, precision, recall, F1 from the confusion matrix) and ROC curves with ROC AUC for a logistic-regression model on the breast-cancer dataset.

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

- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
