# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:10:09 2021

@author: umeshika
"""
#import the libraries
from datetime import datetime 
import numpy as np #import numpy library
from skimage.io import imread
import matplotlib.pyplot as plt

#The variable is create to get the starting time when the code is run
starttime=datetime.now()

img = imread('ouc_pg_convocation.jpg') #load the image
#define function image to plot figures
def image(data,title1, grid_size, grid="on"):
 d=data
 plt.figure()
 plt.title(title1)
 plt.imshow(d)
#define variables for Separate red,green,blue layers  
r=img[:,:,0]#R layer
g=img[:,:,1]#G layer
b=img[:,:,2]#B layer
image(r,"R channel",5) #plot R channel of image 
image(g,"G channel", 5) #plot G channel of image 
image(b,"B channel", 5) #plot B channel of image 
#%%
f_r = np.rot90(img)#rotate image 90'
f_r1 = np.rot90(img, 2)#rotate image 180'
f_r2= np.rot90(img, 3)#rotate image 270'
image(f_r,"The image of 90' rotation",5)#plot 90'rotation of image 
image(f_r1,"The image of 180' rotation",5)#plot 180' rotation of image 
image(f_r2,"The image of 270' rotation",5)#plot 270' rotation of image 
#%%

#the image vertically flips
img_vertical_flip = np.flipud(img)

#the image horizontally flips
img_horizontal_flip = np.fliplr(img)

# plot the flip images
image(img_horizontal_flip, 'The horizontal flip image',5)
image(img_vertical_flip, 'The vertical flip image',5)
           
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    