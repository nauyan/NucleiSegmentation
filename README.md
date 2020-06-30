# Repository for Nuclei Segmentation for Histopathology Images

<p align="center">Note: If you're interested in using it, feel free to ⭐️ the repo so we know!</p>

## Datasets

## Patch Generation
Patch Generation has been done in offline mode to reduce pipeline complexity. The proposed approach uses multiple dataset therefore the size of WSIs are non-standard. Where as the pathches generated from WSIs have dimensions of 256x256x3 having 75% overlap among them. 

## Models
The purpose of this pipeline was to explore and train various nuclei segmentaion datasets therefore we used Modified U-Net for training.
### U-Net
![UNet Architecture](https://vasanashwin.github.io/retrospect/images/unet.png)

## Pre-Trained Models
The Pre-Trained models can be downloaded from [google drive](https://drive.google.com/drive/folders/1g5SdbW8q1Z0e9dk6cW431JO01BDq4g0H).

## Installation
To get this repo work please install all the dependencies using the command below:
```
pip install -U segmentation-models
pip install -r requirments.txt
```

## Training 

## Testing

## Visualization of Results

## Quantitative Results

## Training Plots

## Authors
