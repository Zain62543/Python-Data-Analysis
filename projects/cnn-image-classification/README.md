# Convolutional Neural Networks

Builds CNN image classifiers with the Keras functional API on CIFAR-10, visualises learned features, and then trains a CNN on the Rock-Paper-Scissors image dataset.

| | |
|---|---|
| **Notebook** | [`cnn-cifar10-and-rock-paper-scissors.ipynb`](cnn-cifar10-and-rock-paper-scissors.ipynb) |
| **Data** | CIFAR-10 (`keras.datasets`), Rock-Paper-Scissors (`tensorflow_datasets`), both downloaded at run time |
| **Techniques** | Conv2D / pooling networks, Keras functional API, feature visualisation |
| **Libraries** | TensorFlow/Keras, tensorflow-datasets, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt -r requirements-deep-learning.txt
jupyter lab projects/cnn-image-classification/cnn-cifar10-and-rock-paper-scissors.ipynb
```

## Notes

- Needs TensorFlow; a GPU is recommended. Saved outputs show the original runs.
- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
