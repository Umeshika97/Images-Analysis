# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:03:15 2021

@author: acer
"""
import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage import  color
from skimage.filters import threshold_otsu

page_image = plt.imread('book_page1.png')

# Make the image grayscale using rgb2gray
page_image = color.rgb2gray(page_image)

# Obtain the optimal otsu global thresh value
o = threshold_otsu(page_image)

# Obtain the binary image by applying global thresholding
v = page_image > o

# Show the binary image obtained

#plot the binary image
plt.imshow(v,'Local thresholding')
plt.title("The Book Page Binary Image with lobal thresholding")
plt.axis('off')
plt.show()