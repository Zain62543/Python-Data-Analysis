# Hyperparameter Tuning with Keras Tuner

Uses Keras Tuner's `RandomSearch` to tune an ANN and a CNN (Fashion-MNIST and CIFAR-10 via `keras.datasets`), reports the best hyperparameters and retrains the final models.

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

- Needs TensorFlow and `keras-tuner`; a GPU is recommended.
- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
