# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:23:22 2021

@author: umeshika
"""
#import the libraries
from datetime import datetime 
import numpy as np #import numpy library
from skimage.io import imread
import matplotlib.pyplot as plt
#The variable is create to get the starting time when the code is run
starttime=datetime.now()
#load the images
img = imread('moon.jpg') 
img1 = imread('dark_sky.jpg')

#define hist function for ploting histogram
def histogram(image,title1,ylim):
            plt.hist(image,bins=np.arange(255))
            plt.ylim([0,ylim])
            plt.title(title1)
            plt.xlabel("Pixels Intesity")
            plt.ylabel("Pixels Intesity Count")
            plt.show()
#plot histogram
histogram (img,'HIstogram for moon Image',8)
histogram(img1,'HIstogram for dark sky Image',420)
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    
