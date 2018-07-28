import os
import shutil
from random import shuffle

import Augmentor
import numpy as np
from PIL import Image

data_path = os.path.join('your/image/path/here')

folders = os.listdir(data_path)
DIR_NAME = 'YOUR_DIR_NAME'
# Remove any folder you want to exclude.

classifier_data_path = os.path.join(data_path, DIR_NAME)

if not os.path.exists(classifier_data_path):
    os.mkdir(classifier_data_path)

classifier_train_path = os.path.join(classifier_data_path, 'train')
classifier_val_path = os.path.join(classifier_data_path, 'val')
classifier_test_path = os.path.join(classifier_data_path, 'test')

non_eq_paths = [
    classifier_train_path,
    classifier_val_path,
    classifier_test_path
]

if not os.path.exists(classifier_train_path):
    os.mkdir(classifier_train_path)

if not os.path.exists(classifier_val_path):
    os.mkdir(classifier_val_path)

if not os.path.exists(classifier_test_path):
    os.mkdir(classifier_test_path)


for split in non_eq_paths:
    for folder in folders:
        class_path = os.path.join(split, folder)
        if not os.path.exists(class_path):
            os.mkdir(class_path, mode=777)

def augment_images(path_to_train, target):
    if path_to_train is None:
        raise ValueError('Path to pipeline is null. Aye caramba')

    if target <= 0:
        raise ValueError("Scale should be >= 0.")

    n_original_images = len(os.listdir(path_to_train))

    augmentor = Augmentor.Pipeline(path_to_train)
    augmentor.zoom(probability=0.9, min_factor=1., max_factor=1.25)
    augmentor.flip_left_right(probability=1.)
    augmentor.flip_top_bottom(probability=1.)
    augmentor.shear(probability=0.9, max_shear_left=15, max_shear_right=15)
    augmentor.rotate(probability=1., max_left_rotation=20, max_right_rotation=20)
    augmentor.random_distortion(probability=0.9, grid_width=4, grid_height=4, magnitude=8)
    augmentor.skew(probability=0.9, magnitude=0.4)
    augmentor.sample(target - n_original_images)

    op_folder = os.path.join(path_to_train, 'output')
    augmented_images = os.listdir(op_folder)
    shuffle(augmented_images)

    for augmented_image in augmented_images:
        try:
            # First, rename the image.
            new_name = str(np.random.choice(range(5000))) + '__' + augmented_image
            shutil.move(src=os.path.join(op_folder, augmented_image),
                        dst=os.path.join(op_folder, new_name))

            # Now, move it.
            shutil.move(src=os.path.join(op_folder, new_name),
                        dst=os.path.join(path_to_train, new_name))
        except IOError as e:
            print(e)
            pass

    print('---------------  {} : {}  ---------------'.format(str(path_to_train), target))


for folder in folders:
    images = os.listdir(os.path.join(data_path, folder))
    shuffle(images)
    n_images = len(images)
    train_split = int(n_images * 0.9)
    train_images = images[:train_split]
    test_images = images[train_split:]
    val_split = int(train_split * 0.1)
    shuffle(train_images)
    val_images = train_images[-val_split:]
    new_train_images = train_images[:-val_split]
    for i, train_image in enumerate(new_train_images):
        if (i + 1) % 500 == 0:
            print('{}: Batch of {} images processed'.format(folder, i+1))
        shutil.copy(src=os.path.join(data_path, folder, train_image),
                    dst=os.path.join(classifier_train_path, folder, train_image))

    print('{} Training copy done {} images'.format(folder,
                                                   len(os.listdir(os.path.join(classifier_train_path,
                                                                               folder)))))

    for i, val_image in enumerate(val_images):
        if (i + 1) % 500 == 0:
            print('{}: Batch of {} images processed'.format(folder, i+1))
        shutil.copy(src=os.path.join(data_path, folder, val_image),
                    dst=os.path.join(classifier_val_path, folder, val_image))

    print('{} Validation copy done {} images'.format(folder,
                                                     len(os.listdir(os.path.join(classifier_val_path,
                                                                                 folder)))))

    for i, test_image in enumerate(test_images):
        if (i + 1) % 500 == 0:
            print('{}: Batch of {} images processed'.format(folder, i+1))
        shutil.copy(src=os.path.join(data_path, folder, test_image),
                    dst=os.path.join(classifier_test_path, folder, test_image))

    print('{} Test copy done {} images'.format(folder,
                                                     len(os.listdir(os.path.join(classifier_test_path,
                                                                                 folder)))))


scale = 2
n_augment = {folder:scale*len(os.listdir(os.path.join(classifier_train_path, folder))) for folder in folders}
print(n_augment)

for folder in n_augment.keys():
    augment_images(os.path.join(classifier_train_path, folder), n_augment[folder])


a = input('This is a pause. Please delete the "output" folder')
n_images = 0
mean = np.zeros((450*600*3,), dtype=np.float64)
class_folders = os.listdir(classifier_train_path)
for class_folder in class_folders:
    class_path = os.path.join(classifier_train_path, class_folder)
    images = os.listdir(class_path)
    for image_name in images:
        image = np.asarray(Image.open(os.path.join(class_path, image_name), 'r'))
        mean += image.flatten().astype(np.float64)
        n_images += 1
        if n_images % 500 == 0:
            print('Computed mean of {} images'.format(n_images))

mean = np.divide(mean, np.float64(n_images))
mean_image = np.reshape(mean, (450, 600, 3)).astype(np.float32)
np.savez_compressed('mean_image_' + DIR_NAME + '.npz', image=mean_image)
print('Mean image saved.')


print('------ Script Ended ------')
