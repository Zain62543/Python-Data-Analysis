# Bias, Variance and Over/Underfitting

Explains total error, bias, variance and the trade-off between them. Polynomial fits of degree 1, 3 and 10 on noisy cubic data show under- and overfitting; a `BaggingClassifier` of decision trees on the breast-cancer dataset (with ROC AUC) shows how ensembling reduces variance.

| | |
|---|---|
| **Notebook** | [`bias-variance-polynomial-fits-and-bagging.ipynb`](bias-variance-polynomial-fits-and-bagging.ipynb) |
| **Data** | synthetic noisy cubic data; scikit-learn `load_breast_cancer` |
| **Techniques** | Bias-variance trade-off, polynomial regression, bagging |
| **Libraries** | scikit-learn, pandas, Seaborn, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/bias-variance-tradeoff/bias-variance-polynomial-fits-and-bagging.ipynb
```

- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
