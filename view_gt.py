import scipy.io
import numpy as np
import cv2
import glob
import os
from skimage import io
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np

save_dir = "results/sample_images/"


dataset_name = "cpm15"
dataset_dir = "dataset/cpm15"
prepared_dataset_dir = "prepared_dataset"
images_list = glob.glob(os.path.join(dataset_dir,prepared_dataset_dir,"train","images")+"/*.png")[0]
image = img_to_array(load_img(images_list, color_mode='rgb'))
mask = img_to_array(load_img(os.path.join(dataset_dir,prepared_dataset_dir,"train","masks")+"/"+os.path.basename(images_list), color_mode='grayscale'))
print(image.shape,mask.shape)
io.imsave(os.path.join(save_dir, dataset_name + ".png"), image)
io.imsave(os.path.join(save_dir, dataset_name + "_mask.png"), mask*255.0)

dataset_name = "cpm17"
dataset_dir = "dataset/cpm17"
prepared_dataset_dir = "prepared_dataset"
images_list = glob.glob(os.path.join(dataset_dir,prepared_dataset_dir,"train","images")+"/*.png")[0]
image = img_to_array(load_img(images_list, color_mode='rgb'))
mask = img_to_array(load_img(os.path.join(dataset_dir,prepared_dataset_dir,"train","masks")+"/"+os.path.basename(images_list), color_mode='grayscale'))
print(image.shape,mask.shape)
io.imsave(os.path.join(save_dir, dataset_name + ".png"), image)
io.imsave(os.path.join(save_dir, dataset_name + "_mask.png"), mask*255.0)

dataset_name = "consep"
dataset_dir = "dataset/consep"
prepared_dataset_dir = "prepared_dataset"
images_list = glob.glob(os.path.join(dataset_dir,prepared_dataset_dir,"train","images")+"/*.png")[0]
image = img_to_array(load_img(images_list, color_mode='rgb'))
mask = img_to_array(load_img(os.path.join(dataset_dir,prepared_dataset_dir,"train","masks")+"/"+os.path.basename(images_list), color_mode='grayscale'))
print(image.shape,mask.shape)
io.imsave(os.path.join(save_dir, dataset_name + ".png"), image)
io.imsave(os.path.join(save_dir, dataset_name + "_mask.png"), mask*255.0)

dataset_name = "nucleiseg"
dataset_dir = "dataset/nucleiseg"
prepared_dataset_dir = "prepared_dataset"
images_list = glob.glob(os.path.join(dataset_dir,prepared_dataset_dir,"train","images")+"/*.png")[200]
image = img_to_array(load_img(images_list, color_mode='rgb'))
mask = img_to_array(load_img(os.path.join(dataset_dir,prepared_dataset_dir,"train","masks")+"/"+os.path.basename(images_list), color_mode='grayscale'))
print(image.shape,mask.shape)
io.imsave(os.path.join(save_dir, dataset_name + ".png"), image)
io.imsave(os.path.join(save_dir, dataset_name + "_mask.png"), mask*255.0)


print(np.unique(mask))


