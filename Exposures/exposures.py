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
img = imread('1.jpg') 
img1 = imread('2.jpg') 
img2 = imread('3.jpg') 
img3 = imread('4.jpg') 
img4 = imread('5.jpg') 
img5 = imread('6.jpg') 
img6 = imread('7.jpg') 
img7 = imread('8.jpg') 
img8 = imread('9.jpg') 
img9 = imread('10.jpg') 


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
histogram(img,'HIstogram for exposure Image 1',850000,'Yellow')
histogram(img1,'HIstogram for exposure Image 2',850000,'Yellow')
histogram(img2,'HIstogram for exposure Image 3',850000,'Yellow')
histogram(img3,'HIstogram for exposure Image 4',850000,'Yellow')
histogram(img4,'HIstogram for exposure Image 5',850000,'Yellow')
histogram(img5,'HIstogram for exposure Image 6',850000,'Yellow')
histogram(img6,'HIstogram for exposure Image 7',850000,'Yellow')
histogram(img7,'HIstogram for exposure Image 8',850000,'Yellow')
histogram(img8,'HIstogram for exposure Image 9',850000,'Yellow')
histogram(img9,'HIstogram for exposure Image 10',850000,'Yellow')

"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)  