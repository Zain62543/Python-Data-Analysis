# Iris: EDA, PCA and K-Means

A structured exploratory analysis of the Iris dataset (structure, summary statistics, missing and duplicate values, target distribution, univariate and bivariate analysis, correlations, outliers), followed by preprocessing, PCA and a K-Means clustering introduction on synthetic blobs.

| | |
|---|---|
| **Notebook** | [`eda-pca-kmeans-iris.ipynb`](eda-pca-kmeans-iris.ipynb) |
| **Data** | scikit-learn `load_iris`, `make_blobs` |
| **Techniques** | EDA, dimensionality reduction (PCA), K-Means clustering |
| **Libraries** | pandas, scikit-learn, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/eda-pca-kmeans-iris/eda-pca-kmeans-iris.ipynb
```

## Notes

- The notebook is titled 'Complete Machine Learning Pipeline'; it contains no supervised models.
- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
