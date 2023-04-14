# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:19:10 2021

@author: umeshika
"""
#import the libraries
from datetime import datetime 
import numpy as np #import numpy library
from skimage.io import imread
import matplotlib.pyplot as plt
#from skimage import  color
#import gc
#The variable is create to get the starting time when the code is run
starttime=datetime.now()

img = imread('ouc_pg_convocation.jpg') #load the image
r=img[:,:,0]
g=img[:,:,1]
b=img[:,:,2]
#%%
def histogram(image,title1,ylim,colour):
            plt.hist(image)
            plt.ylim([0,ylim])
            plt.title(title1)
            plt.xlabel("Bins Value")
            plt.ylabel("Pixels Frequency")
            plt.show()
            
histogram(r,'HIstogram for R channel Convocation Image',250,'red')
histogram(g,'HIstogram for G channel Convocation Image',350,'green')  
histogram(b,'HIstogram for B channel Convocation Image',350,'blue')

           
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    
