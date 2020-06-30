import scipy.io
import numpy as np
import cv2
mat = scipy.io.loadmat('dataset/cpm15/cpm15/Labels/image_00.mat')
#print(mat['inst_map'].shape)
unique_elements, counts_elements = np.unique(mat['inst_map'], return_counts=True)
print(unique_elements, counts_elements)
mask = mat['inst_map']
mask[mask>0] = 1
cv2.imwrite("Mask.png",mask*255.0)