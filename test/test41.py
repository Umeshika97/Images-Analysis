# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 18:13:11 2021

@author: Umeshika
"""
#import the libraries
from datetime import datetime 
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
img2 = imread('img_gray.png') #load the image
#plot histogram
plt.hist(img2.ravel(),bins=np.arange(255))
plt.ylim([0,1000])
plt.xlim([-2,260])
plt.title('The histogram for grey toy image')
plt.xlabel("Pixels Intesity")
plt.ylabel("Pixels Intesity Count")
plt.show()