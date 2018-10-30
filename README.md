# SkinLegion
Skin Lesion classification for the ISIC2018 challenge attempted at Persitent Systems

# Members
 - [Bhushan Garware](https://www.linkedin.com/in/bhushan-garware/)
 - [Chinmay Savadikar](https://www.github.com/savadikarc)
 - [Rahul Kulhalli](https://www.github.com/rahulkulhalli)

# Dataset
You may download the HAM10000 dataset from the https://challenge.kitware.com/#phase/5abcbc6f56357d0139260e66 (Note: you will need to register first)

# Notebooks
All our notebooks have been added in the 'Notebooks' folder.

# Scripts
All our preprocessing scripts have been added in the 'Scripts' folder.

# Models
All our trained and fine-tuned models have been added in the 'Models' folder.
*Please note that all the models have been developed in [Keras](https://github.com/keras-team/keras) 2.0.2.*

## Loading a Model ##
To load a saved model, please follow the steps mentioned in the notebooks. As an overview:
1) Define the 'F1', 'Recall', and 'Precision' methods
2) Create a dict in the following way:
```python
custom_obj = {'f1': f1, 'recall': recall, 'precision': precision}
model = load_model('path/to/model.h5', compile=True, custom_objects=custom_obj)
# Model is now loaded into memory.
```
