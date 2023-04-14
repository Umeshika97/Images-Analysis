# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:50:22 2021

@author: umeshika
"""
#import the libraries
from datetime import datetime 
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage import  color
from skimage.filters import threshold_otsu,try_all_threshold,threshold_local

#The variable is create to get the starting time when the code is run
starttime=datetime.now()
img = imread('book_page1.png') #load the image
#the grayscale iamge is taken using rgb2gray
image_gray = color.rgb2gray(img)


#the thresholding image is taken  
binary =image_gray >0.5
#plot the binary image
plt.imshow(binary,cmap='gray')
plt.title("The Book Page Binary Image")
plt.axis('off')
plt.show()

#%% using different method availane in skimage to get binary image
fig1, ax = try_all_threshold(image_gray, verbose=False)
plt.show()
#%%
# take the value of optimal otsu global thresh 
global_thresh = threshold_otsu(image_gray)

# take binary image using global thresholding
binary_global = image_gray > global_thresh

#plot the binary image
plt.imshow(binary_global,cmap='gray')
plt.title("The Book Page Binary Image with global thresholding")
plt.axis('off')
plt.show()



# Set the block size to 35
block_size = 35
# take the value of optimal local thresholding
local_thresh = threshold_local(image_gray, block_size, offset=0.1)

#  take binary image using local thresholding
binary_local = image_gray > local_thresh

#plot the binary image
plt.imshow(binary_local,'Local thresholding')
plt.title("The Book Page Binary Image with lobal thresholding")
plt.axis('off')
plt.show()

print(global_thresh)
print(local_thresh)
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)    


