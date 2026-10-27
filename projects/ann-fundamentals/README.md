# Road to Artificial Neural Networks

Builds up from logistic regression to softmax (multiclass) regression and the perceptron: a manual multiclass example, scikit-learn's `Perceptron` on the Wine dataset, and a single-layer Keras perceptron on the UCI heart-disease data.

| | |
|---|---|
| **Notebook** | [`softmax-regression-to-perceptron-wine-and-heart.ipynb`](softmax-regression-to-perceptron-wine-and-heart.ipynb) |
| **Data** | scikit-learn `load_iris`, `load_wine`, `make_classification`; heart-disease CSV downloaded from GitHub at run time |
| **Techniques** | Softmax regression, perceptron, Keras `Dense` layers |
| **Libraries** | TensorFlow/Keras, scikit-learn, pandas, Seaborn |

## Run it

```bash
# from the repository root
pip install -r requirements.txt -r requirements-deep-learning.txt
jupyter lab projects/ann-fundamentals/softmax-regression-to-perceptron-wine-and-heart.ipynb
```

## Notes

- Needs TensorFlow (`requirements-deep-learning.txt`) and internet access for the heart-disease CSV.
- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
