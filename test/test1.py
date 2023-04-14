# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 21:55:47 2021

@author: umeshika
"""
#import the libraries
from datetime import datetime 
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage import  color
import gc
#The variable is create to get the starting time when the code is run
starttime=datetime.now()
img = imread('face.jpg') #load the image

#%%define the function of imshow1
def imshow1(image, title1, cmap_type='gray'):
          imggray=color.rgb2gray(image)#convert data to gray color
          plt.imshow(imggray, cmap=cmap_type)#take the gray scale image
          plt.title(title1)#label the title
          plt.axis('off')#off the axis
          plt.figure(1) #plot figure
          fig = plt.figure(1)
          plt.show()
          return fig
#gray color image is taken using imshow1 function          
imshow1(img,"face",cmap_type='gray') 
#save the gray color image different location
fig=imshow1(img,"face",cmap_type='gray') 
fig.savefig('E:/Third Year/Second Semester/PH 3034 Digital Image Processing 1/week 03/faceimage.png')
#load the saved image
img2=imread('E:/Third Year/Second Semester/PH 3034 Digital Image Processing 1/week 03/faceimage.png')
#The saved grayscale image is Converted into a grayscale 
image2=color.rgb2gray(img2)
plt.imshow(image2, cmap='gray')#take the gray scale image
plt.title("gray color image 2")#label the title
plt.axis('off')#off the axis
plt.figure(2)#plot figure 
plt.show()#show image

gc.collect()#Clear memory of the IDE
#Load both RGB and grayscale images two variables I1 and I2
I1=imread('face.jpg')
I2=imread('E:/Third Year/Second Semester/PH 3034 Digital Image Processing 1/week 03/faceimage.png')
#take the dimensions of them 
print(I1.shape) 
print(I2.shape) 

"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    

   