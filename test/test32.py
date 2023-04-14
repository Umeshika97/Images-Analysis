# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 05:44:38 2021

@author: Umeshika
"""
#import the libraries
from datetime import datetime 
import numpy as np 
from skimage.io import imread
import matplotlib.pyplot as plt

#The variable is create to get the starting time when the code is run
starttime=datetime.now()
img = imread('The Contrast Stretched Image.png') #load the image
def histogram(imagehis,title1,ylim):
            plt.hist(imagehis.ravel(),bins=np.arange(255))
            plt.ylim([0,ylim])
            plt.xlim([-2,260])
            plt.title(title1)
            plt.xlabel("Pixels Intesity")
            plt.ylabel("Pixels Intesity Count")
            plt.show()
#plot histogram            
histogram(img,'HIstogram for Contrast Stretched Village Image',25000)
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    

