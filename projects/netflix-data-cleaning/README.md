# Netflix Catalogue: Data Cleaning Case Study

Loads and profiles Netflix's titles catalogue, handles missing values with `dropna` / `fillna`, parses the `duration` and `date_added` columns and derives a content-age feature. The notebook is a training case study, so the 'client brief' at the top is part of the exercise, not a real engagement.

| | |
|---|---|
| **Notebook** | [`netflix-data-cleaning.ipynb`](netflix-data-cleaning.ipynb) |
| **Data** | `data/netflix_titles_homework.csv` (6,234 titles x 12 columns) |
| **Techniques** | Data profiling, missing-value handling, column parsing, feature derivation |
| **Libraries** | pandas |

## Run it

```bash
# from the repository root
pip install -r requirements.txt
jupyter lab projects/netflix-data-cleaning/netflix-data-cleaning.ipynb
```

## Notes

- Covers Section 1 of the brief (familiarisation and cleaning) only.
- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
