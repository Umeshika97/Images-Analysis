# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 19:19:15 2021

@author: umeshika
"""
#import the libraries
from datetime import datetime 
import numpy as np 
from skimage.io import imread
import matplotlib.pyplot as plt

#The variable is create to get the starting time when the code is run
starttime=datetime.now()
#load the images
img = imread('50.jpg') 
img1 = imread('80.jpg') 
img2 = imread('100.jpg') 
img3 = imread('160.jpg') 
img4 = imread('250.jpg') 
img5 = imread('400.jpg') 
img6 = imread('640.jpg') 
img7 = imread('800.jpg') 
img8 = imread('1600.jpg') 
img9 = imread('3200.jpg') 


#define function to plot histogram
def histogram(imagehis,title1,ylim,colour):
            plt.hist(imagehis.ravel(),bins=np.arange(255), color=colour)
            plt.ylim([0,ylim])
            plt.xlim([-2,260])
            plt.title(title1)
            plt.xlabel("Pixels Intesity")
            plt.ylabel("Pixels Intesity Count")
            plt.show()

#plot histogram for diffrent ISO levels         
histogram(img,'HIstogram for ISO level 50 Image',850000,'purple')
histogram(img1,'HIstogram for ISO level 80 Image',850000,'purple')
histogram(img2,'HIstogram for ISO level 100 Image',850000,'purple')
histogram(img3,'HIstogram for ISO level 160 Image',850000,'purple')
histogram(img4,'HIstogram for ISO level 250 Image',850000,'purple')
histogram(img5,'HIstogram for ISO level 400 Image',850000,'purple')
histogram(img6,'HIstogram for ISO level 640 Image',850000,'purple')
histogram(img7,'HIstogram for ISO level 800 Image',850000,'purple')
histogram(img8,'HIstogram for ISO level 1600 Image',850000,'purple')
histogram(img9,'HIstogram for ISO level 3200 Image',850000,'purple')

"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)  