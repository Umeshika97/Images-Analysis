# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 19:19:15 2021

@author: umeshika
"""
#import the libraries
from datetime import datetime 
import numpy as np 
import cv2
from skimage.io import imread
import matplotlib.pyplot as plt

#The variable is create to get the starting time when the code is run
starttime=datetime.now()
img = imread('village.bmp') #load the image
def histogram(imagehis,title1,ylim,colour):
            plt.hist(imagehis.ravel(),bins=np.arange(255), color=colour)
            plt.ylim([0,ylim])
            plt.xlim([-2,260])
            plt.title(title1)
            plt.xlabel("Pixels Intesity")
            plt.ylabel("Pixels Intesity Count")
            plt.show()
#plot histogram            
histogram(img,'HIstogram for Village Image',25000,'purple')
#%%

# Read the image
img2 = cv2.imread('village.bmp',0)

def image(imageplot,title1,grid="on"):
 plt.figure()
 plt.title(title1)
 plt.imshow(imageplot)

# stretched image Creates with zeros array to store  
r_min_max= np.zeros((img2.shape[0],img2.shape[1]),dtype = 'uint8')

# apply Min-Max formulae using Loop over the image 
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        r_min_max[i,j] = 255*(img2[i,j]-np.min(img2))/(np.max(img2)-np.min(img2))

# plot the Contrast stretched image
image(r_min_max,'The Contrast Stretched Image')
cv2.imshow('The Contrast Stretched Image',r_min_max)
#save the image
cv2.imwrite('The Contrast Stretched Image.png', r_min_max)

cv2.waitKey(0)
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    
