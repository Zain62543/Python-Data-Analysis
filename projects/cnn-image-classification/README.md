# Convolutional Neural Networks

Builds CNN image classifiers with the Keras functional API on CIFAR-10 and Rock-Paper-Scissors, with seeds, a deterministic shuffled validation split, per-class reports / confusion matrices and feature-map visualisation.

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

- Needs TensorFlow; a GPU is recommended. Revised (seeds, deterministic validation split, per-class evaluation) but **not re-run**: unchanged CIFAR-10 cells keep outputs from an earlier unseeded run, changed cells have empty outputs.
- Methodology reviewed and revised, but **not re-run** (TensorFlow unavailable); see the banner at the top of the notebook for which outputs are from an earlier run.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
