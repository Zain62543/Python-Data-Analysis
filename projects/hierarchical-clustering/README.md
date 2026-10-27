# Hierarchical Clustering

Covers agglomerative clustering: distance metrics, linkage criteria, dendrograms with a cut line, and `AgglomerativeClustering`. On Iris it compares linkages and raw vs standardised features (silhouette, cophenetic correlation, ARI) and validates clusters against the species with a contingency table, ARI and NMI.

| | |
|---|---|
| **Notebook** | [`hierarchical-clustering-linkage-and-dendrograms.ipynb`](hierarchical-clustering-linkage-and-dendrograms.ipynb) |
| **Data** | scikit-learn `load_iris`, `make_blobs` |
| **Techniques** | Agglomerative clustering, dendrograms, linkage methods, PCA |
| **Libraries** | scikit-learn, SciPy, pandas, Seaborn, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/hierarchical-clustering/hierarchical-clustering-linkage-and-dendrograms.ipynb
```

- Methodology reviewed and revised; the notebook was **executed end-to-end** and the saved outputs come from that run (Python 3.13, scikit-learn 1.9, pandas 3.0).
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
