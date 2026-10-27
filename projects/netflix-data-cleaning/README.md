# Netflix Catalogue: Data Cleaning Case Study

Loads and profiles Netflix's titles catalogue, applies a documented column-by-column missing-value policy (with row counts lost), parses `duration` into movie minutes and TV seasons (left missing where not applicable, with assertions), and derives content-age, era and recency features. The 'client brief' is part of a training exercise, not a real engagement.

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
- Methodology reviewed and revised; the notebook was **executed end-to-end** and the saved outputs come from that run (Python 3.13, scikit-learn 1.9, pandas 3.0).
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
