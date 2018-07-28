import os
import shutil
from random import shuffle

train_data = os.path.join('path/to/your/train/dir')
# This will create a folder in the following location.
toy_path = os.path.join('path/to/your/toy/train/dir')
toy_path_pos = os.path.join('path/to/your/toy/train/dir/pos')
toy_path_neg = os.path.join('path/to/your/toy/train/dir/neg')

os.makedirs(toy_path)
os.makedirs(os.path.join(toy_path_pos))
os.makedirs(os.path.join(toy_path_neg))

classes = os.listdir(train_data)
for class_name in classes:
    image_path = os.path.join(train_data, class_name)
    images = os.listdir(image_path)
    shuffle(images)
    toy_set = images[:int(0.2 * len(images))]

    for toy_img in toy_set:
        shutil.copy(src=os.path.join(image_path, toy_img), dst=os.path.join(toy_path, class_name, toy_img))

    print('Copied ' + class_name)
