# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:19:10 2021

@author: umeshika
"""
#import the libraries
from datetime import datetime 
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

#The variable is create to get the starting time when the code is run
starttime=datetime.now()
img = imread('ouc_pg_convocation.jpg') #load the image
#define variables for Separate three RGB layers 
r=img[:,:,0]#R layer
g=img[:,:,1]#G layer
b=img[:,:,2]#B layer
#%%define hist function for ploting histogram
def histogram(image,title1,ylim,colour):
            plt.hist(image.ravel(),bins=np.arange(255), color=colour)
            plt.ylim([0,ylim])
            plt.xlim([-2,260])
            plt.title(title1)
            plt.xlabel("Pixels Intesity")
            plt.ylabel("Pixels Intesity Count")
            plt.show()
#plot histogram            
histogram(r,'HIstogram for R channel Convocation Image',8000,'red')
histogram(g,'HIstogram for G channel Convocation Image',40000,'green')  
histogram(b,'HIstogram for B channel Convocation Image',7000,'blue')

           
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    
