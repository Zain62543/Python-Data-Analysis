# Iris: EDA, PCA and K-Means

Exploratory analysis of the Iris data (structure, duplicates, class balance, pairwise plots, correlations), then K-Means clustering: K chosen with elbow and silhouette together, scaling and seed stability compared, and results validated against the species with ARI / NMI and a contingency table. PCA is used for visualisation.

| | |
|---|---|
| **Notebook** | [`iris-eda-pca-and-kmeans.ipynb`](iris-eda-pca-and-kmeans.ipynb) |
| **Data** | scikit-learn `load_iris`, `make_blobs` |
| **Techniques** | EDA, K-Means, elbow / silhouette, cluster validation (ARI, NMI), PCA |
| **Libraries** | pandas, scikit-learn, Seaborn, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/eda-pca-kmeans-iris/iris-eda-pca-and-kmeans.ipynb
```

## Notes

- Clustering has no train/test split; labels are used only to validate the result.
- Methodology reviewed and revised; the notebook was **executed end-to-end** and the saved outputs come from that run (Python 3.13, scikit-learn 1.9, pandas 3.0).
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
