# Air Quality: Missing-Data Analysis

Profiles the missing values of a daily air-quality series, tests whether the missingness is random, and compares five imputation methods (mean, median, time interpolation, KNN, iterative) by hiding known ozone values and measuring the error over 30 random masks. Outliers are then flagged with IQR, z-score and MAD rules on the raw and log scales, and flagged rather than deleted.

| | |
|---|---|
| **Notebook** | [`air-quality-missing-data-and-outliers.ipynb`](air-quality-missing-data-and-outliers.ipynb) |
| **Data** | `data/airQuality.csv` (153 daily rows, May-Sep 1973: Ozone, Solar.R, Wind, Temp; original Month/Day layout, reconstructed, see `DATA.md`) |
| **Techniques** | Missingness diagnostics, imputation benchmarking by masking, outlier detection (IQR / z-score / MAD) |
| **Libraries** | pandas, NumPy, SciPy, scikit-learn, Matplotlib, Seaborn |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/air-quality-missing-data/air-quality-missing-data-and-outliers.ipynb
```

## Notes

- The earlier draft that also covered Wine feature selection is kept unedited in `learning-archive/classical-ml/20-...`.
- Methodology reviewed and revised; the notebook was **executed end-to-end** and the saved outputs come from that run (Python 3.13, scikit-learn 1.9, pandas 3.0).
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
