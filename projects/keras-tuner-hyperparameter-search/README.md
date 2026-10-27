# Hyperparameter Tuning with Keras Tuner

Uses Keras Tuner's `RandomSearch` on a stratified 10k subset to tune an ANN (Fashion-MNIST) and a CNN (CIFAR-10), retrains the best configuration on the full training set with early stopping, and evaluates once on the test set against a baseline.

| | |
|---|---|
| **Notebook** | [`keras-tuner-ann-fashion-mnist-and-cnn-cifar10.ipynb`](keras-tuner-ann-fashion-mnist-and-cnn-cifar10.ipynb) |
| **Data** | Fashion-MNIST and CIFAR-10 (`keras.datasets`), downloaded at run time |
| **Techniques** | Random search, hyperparameter spaces, final retraining |
| **Libraries** | TensorFlow/Keras, keras-tuner |

## Run it

```bash
# from the repository root
pip install -r requirements.txt -r requirements-deep-learning.txt
jupyter lab projects/keras-tuner-hyperparameter-search/keras-tuner-ann-fashion-mnist-and-cnn-cifar10.ipynb
```

## Notes

- Needs TensorFlow and `keras-tuner`; a GPU is recommended. Revised (stratified tuning subset, seeds, early stopping, baseline) but **not re-run**: all outputs are cleared.
- Methodology reviewed and revised, but **not re-run** (TensorFlow unavailable); all outputs are cleared.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
