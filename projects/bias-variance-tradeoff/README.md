# Bias, Variance and Over/Underfitting

Explains total error, bias and variance, then measures them **by simulation** on a known cubic function (bias², variance and noise per polynomial degree), shows validation and learning curves with shuffled folds, and compares a single tree with bagging on the breast-cancer data using repeated CV.

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

- Methodology reviewed and revised; the notebook was **executed end-to-end** and the saved outputs come from that run (Python 3.13, scikit-learn 1.9, pandas 3.0).
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
