# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 13:59:50 2021

@author: Umeshika
"""
#import the libraries
from datetime import datetime 
from skimage.io import imread
import numpy as np 
import matplotlib.pyplot as plt
from skimage import  color
from skimage.filters import threshold_otsu,try_all_threshold

#The variable is create to get the starting time when the code is run
starttime=datetime.now()
img1 = imread('toys1.jpg') #load the image

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
#imshow1(img1,"The Toys Image",cmap_type='gray') 
#save the gray color image different location
fig=imshow1(img1,"The Toys Gray Image",cmap_type='gray') 
fig.savefig('img_gray1.png')

img2 = imread('img_gray1.png') #load the image
plt.hist(img2.ravel(),bins=np.arange(255))
plt.ylim([0,12000])
plt.xlim([-2,260])
plt.title('The histogram for grey scale toy image')
plt.xlabel("Pixels Intesity")
plt.ylabel("Pixels Intesity Count")
plt.show()
#%%
#the grayscale iamge is taken using rgb2gray
toyimage_gray = color.rgb2gray(img1)

# take threshold value with otsu
threshimage = threshold_otsu(toyimage_gray)

#the thresholding image is taken  
binary =toyimage_gray > 0.5
#plot the binary image
plt.imshow(binary,cmap='gray')
plt.title("The Toys Binary Image")
plt.axis('off')
plt.show()
print(threshimage)
#%% using different method availane in skimage to get binary image
fig1, ax = try_all_threshold(toyimage_gray, verbose=False)
plt.show()


"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    

