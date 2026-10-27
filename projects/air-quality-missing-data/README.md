# Air Quality: Missing-Data Analysis

Visualises and analyses missing values in a daily air-quality time series, then works through transforming, processing, feature engineering and outlier analysis. A final section demonstrates scaling and model-based feature selection on scikit-learn's Wine dataset.

| | |
|---|---|
| **Notebook** | [`air-quality-missing-data-and-outliers.ipynb`](air-quality-missing-data-and-outliers.ipynb) |
| **Data** | `data/air-quality.csv` (153 daily rows, May-Sep 1973: Ozone, Solar.R, Wind, Temp) and `data/airQuality.csv` (same data in its original Month/Day layout, reconstructed; see `DATA.md`) |
| **Techniques** | Missing-data visualisation, outlier analysis, scaling, `SelectFromModel` with a random forest |
| **Libraries** | pandas, missingno, SciPy, scikit-learn, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/air-quality-missing-data/air-quality-missing-data-and-outliers.ipynb
```

## Notes

- Needs `missingno` (in `requirements.txt`).
- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
