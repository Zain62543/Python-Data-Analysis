# Road to Artificial Neural Networks

Builds up from logistic regression to softmax regression and the perceptron (scikit-learn, with baselines and repeated CV), then a single sigmoid neuron in Keras on the UCI heart-disease data, compared on the same split with logistic regression and a sklearn perceptron.

| | |
|---|---|
| **Notebook** | [`softmax-regression-to-perceptron-wine-and-heart.ipynb`](softmax-regression-to-perceptron-wine-and-heart.ipynb) |
| **Data** | scikit-learn `load_iris`, `load_wine`, `make_classification`; `data/heart.csv` |
| **Techniques** | Softmax regression, perceptron, Keras `Dense` layers |
| **Libraries** | TensorFlow/Keras, scikit-learn, pandas, Seaborn |

## Run it

```bash
# from the repository root
pip install -r requirements.txt -r requirements-deep-learning.txt
jupyter lab projects/ann-fundamentals/softmax-regression-to-perceptron-wine-and-heart.ipynb
```

## Notes

- Methodology reviewed and revised. The notebook was **executed end-to-end** (the Keras cells on a Colab GPU) and all outputs are saved. Keras results vary slightly between runs; the cross-validated scikit-learn tables are the more reliable comparison.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
