import os
import shutil
import pandas as pd

GROUND_TRUTH_LABEL_CSV = os.path.join('path/to/ISIC2018_Task3_Training_GroundTruth.csv')

IMAGES_DIR = os.path.join('path/to/ISIC2018_Task3_Training_Input')

print('A total of {} images visible.'.format(str(len(os.listdir(IMAGES_DIR)))))


def get_or_create_folder(path):
    # Check whether the directories have been created.
    if not os.path.exists(path):
        print("{} is not present. Creating directory...".format(str(path)))
        os.mkdir(path=path)
    else:
        print("{} is already present.".format(str(path)))


def copy_to_path(image_names, folder_name):
    for image in image_names:
        shutil.copy(src=os.path.join(IMAGES_DIR, image + '.jpg'),
                    dst=os.path.join('path/to/ISIC2018',
                                     'output', folder_name, image + '.jpg'))

    print('Copied {} images to {}'.format(str(len(image_names)), folder_name))


# Create the directories (if not already present).
print('-------------------------------')
print('Creating directories...')
print('-------------------------------')
get_or_create_folder(os.path.join('path/to/ISIC2018/output'))
get_or_create_folder(os.path.join('path/to/ISIC2018/output', 'MEL'))
get_or_create_folder(os.path.join('path/to/ISIC2018/output', 'NV'))
get_or_create_folder(os.path.join('path/to/ISIC2018/output', 'AKIEC'))
get_or_create_folder(os.path.join('path/to/ISIC2018/output', 'BKL'))
get_or_create_folder(os.path.join('path/to/ISIC2018/output', 'BCC'))
get_or_create_folder(os.path.join('path/to/ISIC2018/output', 'DF'))
get_or_create_folder(os.path.join('path/to/ISIC2018/output', 'VASC'))
print('-------------------------------')

# Read the csv.
df = pd.read_csv(GROUND_TRUTH_LABEL_CSV)

# Get the image names where a particular column is 1.
mel_image_names = (df['image'].where(df['MEL'] == 1.)).dropna().tolist()
nv_image_names = (df['image'].where(df['NV'] == 1.)).dropna().tolist()
akiec_image_names = (df['image'].where(df['AKIEC'] == 1.)).dropna().tolist()
bkl_image_names = (df['image'].where(df['BKL'] == 1.)).dropna().tolist()
bcc_image_names = (df['image'].where(df['BCC'] == 1.)).dropna().tolist()
df_image_names = (df['image'].where(df['DF'] == 1.)).dropna().tolist()
vasc_image_names = (df['image'].where(df['VASC'] == 1.)).dropna().tolist()

# Copy images from src to dst.
print('Copying images to the folders...')
print('-------------------------------')
copy_to_path(mel_image_names, 'MEL')
copy_to_path(nv_image_names, 'NV')
copy_to_path(akiec_image_names, 'AKIEC')
copy_to_path(bkl_image_names, 'BKL')
copy_to_path(bcc_image_names, 'BCC')
copy_to_path(df_image_names, 'DF')
copy_to_path(vasc_image_names, 'VASC')
print('-------------------------------')
print('Script has finished running.')
print('-------------------------------')
