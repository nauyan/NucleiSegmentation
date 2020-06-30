import glob
import os
import numpy as np
from skimage import io
#from src.network.unet.unet import get_unet
from sklearn.model_selection import train_test_split
import progressbar

import segmentation_models as sm

import keras
from keras.optimizers import Adam,SGD
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

import matplotlib.pyplot as plt
from src.utils.metrics import *
from src.utils.lossfunctions import *
# or from tensorflow import keras

keras.backend.set_image_data_format('channels_last')

#dataset_name = "cpm15"
#dataset_dir = "dataset/cpm15"
#dataset_name = "cpm17"
#dataset_dir = "dataset/cpm17"
#dataset_name = "consep"
#dataset_dir = "dataset/consep"
dataset_name = "nucleiseg"
dataset_dir = "dataset/nucleiseg"
prepared_dataset_dir = "prepared_dataset"

images_list = glob.glob(os.path.join(dataset_dir,prepared_dataset_dir,"train","images")+"/*.png")
#print(images_list)

X_train = []
y_train = []
for image_path in progressbar.progressbar(images_list):
    #image = io.imread(image_path)
    image = img_to_array(load_img(image_path, color_mode='rgb'))
    image = image/255.0

    mask = img_to_array(load_img(os.path.join(dataset_dir,prepared_dataset_dir,"train","masks")+"/"+os.path.basename(image_path), color_mode='grayscale'))
    #print(np.unique(mask, return_counts=True))
    mask = mask.reshape(mask.shape[0],mask.shape[1],1)
    #print(image.shape,mask.shape)
    
    X_train.append(image)
    y_train.append(mask)

X_train = np.array(X_train)
y_train = np.array(y_train)
print("Loaded Training Data")


images_list = glob.glob(os.path.join(dataset_dir,prepared_dataset_dir,"test","images")+"/*.png")

X_test = []
y_test = []
for image_path in progressbar.progressbar(images_list):
    #image = io.imread(image_path)
    image = img_to_array(load_img(image_path, color_mode='rgb'))
    image = image/255.0

    mask = img_to_array(load_img(os.path.join(dataset_dir,prepared_dataset_dir,"test","masks")+"/"+os.path.basename(image_path), color_mode='grayscale'))
    #print(np.unique(mask, return_counts=True))
    mask = mask.reshape(mask.shape[0],mask.shape[1],1)
    #print(image.shape,mask.shape)
    
    X_test.append(image)
    y_test.append(mask)

X_test = np.array(X_test)
y_test = np.array(y_test)
print("Loaded Test Data")
#print(Images.shape,Labels.shape)


#X_train, X_test, y_train, y_test = train_test_split(Images, Labels, test_size=0.1)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

model = sm.Unet('efficientnetb0', classes=1, activation='sigmoid')



model.compile(
    Adam(),
    loss=jaccard_distance_loss,
    metrics=["accuracy", dice_coef, f1],
)

callbacks = [
    EarlyStopping(patience=10, verbose=1),
    ReduceLROnPlateau(factor=0.1, patience=5, min_lr=0.00001, verbose=1),
    ModelCheckpoint('./results/weights/'+str(dataset_name)+'_Best.h5', monitor='val_loss', mode = 'min' , verbose=1, save_best_only=True, save_weights_only=False)
]

results = model.fit(
   x=X_train,
   y=y_train,
   batch_size=16,
   epochs=100,
   validation_data=(X_test, y_test),
   callbacks=callbacks
)

print(model.evaluate(X_test, y_test, verbose=1))

plt.figure(figsize=(8, 8))
plt.title("Learning curve")
plt.plot(results.history["loss"], label="loss")
plt.plot(results.history["val_loss"], label="val_loss")
plt.plot( np.argmin(results.history["val_loss"]), np.min(results.history["val_loss"]), marker="x", color="r", label="best model")
plt.xlabel("Epochs")
plt.ylabel("log_loss")
plt.legend();
plt.savefig('./results/plots/'+str(dataset_name)+'_train_loss.png')

plt.figure(figsize=(8, 8))
plt.title("Learning curve")
plt.plot(results.history["dice_coef"], label="dice_coef")
plt.plot(results.history["val_dice_coef"], label="val_dice_coef")
plt.plot( np.argmax(results.history["val_dice_coef"]), np.max(results.history["val_dice_coef"]), marker="x", color="r", label="best model")
plt.xlabel("Epochs")
plt.ylabel("Dice Coeff")
plt.legend();
plt.savefig('./results/plots/'+str(dataset_name)+'_train_dice.png')

plt.figure(figsize=(8, 8))
plt.title("Learning curve")
plt.plot(results.history["f1"], label="f1")
plt.plot(results.history["val_f1"], label="val_f1")
plt.plot( np.argmax(results.history["val_f1"]), np.max(results.history["val_f1"]), marker="x", color="r", label="best model")
plt.xlabel("Epochs")
plt.ylabel("f1")
plt.legend();
plt.savefig('./results/plots/'+str(dataset_name)+'_train_f1.png')

plt.figure(figsize=(8, 8))
plt.title("Learning curve")
plt.plot(results.history["accuracy"], label="accuracy")
plt.plot(results.history["val_accuracy"], label="val_accuracy")
plt.plot( np.argmax(results.history["val_accuracy"]), np.max(results.history["val_accuracy"]), marker="x", color="r", label="best model")
plt.xlabel("Epochs")
plt.ylabel("accuracy")
plt.legend();
plt.savefig('./results/plots/'+str(dataset_name)+'_train_accuracy.png')
