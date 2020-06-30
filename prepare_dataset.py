from skimage.util.shape import view_as_windows
from skimage import img_as_ubyte

import os
import glob
import scipy.io
import numpy as np
from skimage import io
import cv2 

from sklearn.model_selection import train_test_split

patch_width = 256
patch_height = 256

dataset_dir = "dataset/cpm15"
img_dir = "cpm15/Images"
label_dir = "cpm15/Labels"

prepared_dataset_dir = "prepared_dataset"
#print()
image_list = glob.glob(os.path.join(dataset_dir,img_dir)+"/*.png")
#print(image_list)
for img_path in image_list:
    image = io.imread(img_path)
    
    label_path = glob.glob(os.path.join(dataset_dir,label_dir,os.path.splitext(os.path.basename(img_path))[0])+"*")[0]
    #print(label_path)
    label = scipy.io.loadmat(label_path)
    label = label['inst_map']
    label = label.reshape(label.shape[0],label.shape[1],1)
    #print(image.shape,label.shape)
    
    patches = view_as_windows(np.concatenate((image, label[:,:,0].reshape(image.shape[0],image.shape[1],1)), axis=2),
                    (patch_width, patch_height, 4), (patch_width//4, patch_height//4, 4))
    patches = patches.reshape(-1,patch_width,patch_height,4)
    
    print(patches.shape)
    
    for idx,patch in enumerate(patches):
        io.imsave(os.path.join(dataset_dir,prepared_dataset_dir,"images",os.path.splitext(os.path.basename(img_path))[0]+"_"+str(idx)+".png"),img_as_ubyte(patch[:,:,0:3]))
        temp_mask = patch[:,:,3]
        temp_mask[temp_mask>0] = 1
        #io.imsave(os.path.join(dataset_dir,prepared_dataset_dir,"masks",os.path.splitext(os.path.basename(img_path))[0]+"_"+str(idx)+".png"),temp_mask)
        cv2.imwrite(os.path.join(dataset_dir,prepared_dataset_dir,"masks",os.path.splitext(os.path.basename(img_path))[0]+"_"+str(idx)+".png"),temp_mask)
