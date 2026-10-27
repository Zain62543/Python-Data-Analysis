# Transfer Learning: Feature Extraction and Fine-Tuning

Explains transfer learning, then compares feature extraction (frozen VGG16) with two-stage fine-tuning of ResNet50 on the filtered cats-vs-dogs dataset, using model-specific preprocessing, a validation / test split, early stopping, and one test evaluation for the model chosen on validation.

| | |
|---|---|
| **Notebook** | [`transfer-learning-vgg16-and-resnet50-cats-vs-dogs.ipynb`](transfer-learning-vgg16-and-resnet50-cats-vs-dogs.ipynb) |
| **Data** | `cats_and_dogs_filtered.zip` (Google-hosted), downloaded at run time |
| **Techniques** | Pretrained CNNs, feature extraction, fine-tuning |
| **Libraries** | TensorFlow/Keras, Matplotlib |

## Run it

```bash
# from the repository root
pip install -r requirements.txt -r requirements-deep-learning.txt
jupyter lab projects/transfer-learning/transfer-learning-vgg16-and-resnet50-cats-vs-dogs.ipynb
```

## Notes

- Needs TensorFlow, a GPU and internet access. Rewritten to fix preprocessing, data-split and fine-tuning issues (listed at the end of the notebook) but **not yet run**: all outputs are cleared.
- Rewritten to fix methodological problems, but **not yet run** (TensorFlow, GPU and download unavailable); all outputs are cleared.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
