# Hierarchical Clustering

Covers the intuition and maths of agglomerative clustering: distance metrics, linkage criteria (Ward, single, complete, average), dendrograms and `AgglomerativeClustering`, with PCA for visualisation and a confusion matrix against the true Iris species.

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

- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
