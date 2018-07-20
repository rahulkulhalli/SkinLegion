import os
import shutil
from random import shuffle

train_data = os.path.join('D:\\', 'ISIC2018', 'output', 'output', 'nv_non_nv', 'train')
toy_path = os.path.join('D:\\', 'ISIC2018', 'output', 'output', 'nv_non_nv', 'toy_train')
toy_path_nv = os.path.join('D:\\', 'ISIC2018', 'output', 'output', 'nv_non_nv', 'toy_train', 'NV')
toy_path_non_nv = os.path.join('D:\\', 'ISIC2018', 'output', 'output', 'nv_non_nv', 'toy_train', 'NON_NV')

os.makedirs(toy_path)
os.makedirs(os.path.join(toy_path_nv))
os.makedirs(os.path.join(toy_path_non_nv))

classes = os.listdir(train_data)
for class_name in classes:
    image_path = os.path.join(train_data, class_name)
    images = os.listdir(image_path)
    shuffle(images)
    toy_set = images[:int(0.2 * len(images))]

    for toy_img in toy_set:
        shutil.copy(src=os.path.join(image_path, toy_img), dst=os.path.join(toy_path, class_name, toy_img))

    print('Copied ' + class_name)