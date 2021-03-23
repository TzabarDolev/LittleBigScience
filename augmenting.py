from imgaug import augmenters as iaa
import numpy as np
import os
import cv2

img_folder = 'data/hymenoptera_data/val/ants/'
output_folder = 'data/hymenoptera_data/val_aug/ants/'
images = os.listdir(img_folder)
images.sort()

seq1 = iaa.Sequential([
    iaa.Fliplr(),
    iaa.Fog()
])

for img_ind in range(len(images)-1):

    img = cv2.imread(str(img_folder) + images[img_ind])
    img_aug = seq1.augment_images(img)

    cv2.imwrite(output_folder + images[img_ind], img_aug)

