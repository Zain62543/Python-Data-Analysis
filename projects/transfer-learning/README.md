# Transfer Learning: Feature Extraction and Fine-Tuning

Explains transfer learning, then works two case studies on the filtered cats-vs-dogs image dataset: feature extraction with a pretrained VGG16 and fine-tuning ResNet50, with evaluation plots and a note on overfitting.

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

- Needs TensorFlow and internet access; a GPU is recommended.
- Saved outputs are from the original runs; the notebook was not re-executed after the repository was reorganised.
- Data paths are relative (`../../data/...`) so the notebook runs from its own folder.

[Back to all projects](../../README.md)
