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
imgs = imread('1_16000.jpg') 
imgs1 = imread('2_12000.jpg') 
imgs2 = imread('3_2000.jpg') 
imgs3 = imread('4_1000.jpg') 
imgs4 = imread('5_500.jpg') 
imgs5 = imread('6_250.jpg') 
imgs6 = imread('7_125.jpg') 
imgs7 = imread('8_60.jpg') 
imgs8 = imread('9_45.jpg') 
imgs9 = imread('10_10.jpg') 


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
histogram(imgs,'HIstogram for 1/16000 s Shutter Speed of Image',10000000,'deepskyblue')
histogram(imgs1,'HIstogram for 1/12000 s Shutter Speed of Image',10000000,'deepskyblue')
histogram(imgs2,'HIstogram for 1/2000 s Shutter Speed of Image',1500000,'deepskyblue')
histogram(imgs3,'HIstogram for 1/1000 s Shutter Speed of Image',1500000,'deepskyblue')
histogram(imgs4,'HIstogram for 1/500 s Shutter Speed of Image',850000,'deepskyblue')
histogram(imgs5,'HIstogram for 1/250 s Shutter Speed ofImage',850000,'deepskyblue')
histogram(imgs6,'HIstogram for 1/125 s Shutter Speed of Image',850000,'deepskyblue')
histogram(imgs7,'HIstogram for 1/60 s Shutter Speed of Image',850000,'deepskyblue')
histogram(imgs8,'HIstogram for 1/45 s Shutter Speed of Image',1000000,'deepskyblue')
histogram(imgs9,'HIstogram for 1/20 s Shutter Speed of Image',1000000,'deepskyblue')
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)  