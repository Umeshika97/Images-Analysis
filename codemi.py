# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:17:10 2021

@author: umeshika
"""
import numpy as np #import numpy library
import matplotlib.pyplot as plt #import matplotlib for graph plotting
import datetime #import datetime for time measurements
start = datetime.datetime.now() #record the starting time of the code
"""
function to extract images and apply gridlines and its colors as wished.
The function of the code snippet is explained on the section 2.3.1.
"""
def image(data,title1, grid_size, grid="on"):
 d=data
 plt.figure()
 plt.title(title1)
 plt.imshow(d, extent=[0,d.shape[0], d.shape[1],0])

if __name__ == '__main__':

 img= plt.imread("archie_pix.jpg") #extract image info
 f = np.array(img) #extract image info to an array

#defining kernel
g = np.array([[1/16,1/8,1/16],
              [1/8,1/4,1/8],
              [1/16,1/8,1/16]]) 

image(f[:,:,0],"rr", 5) #display the first layer of image in grayscale
image(f[:,:,1],"gg", 5) #display the second layer of image in grayscale
image(f[:,:,2],"BB", 5) #display the third layer of image in grayscale
g_r = np.rot90(g, 2) #reversing kernel

#define different image layers and assign to variables
f_0 = f[:,:,0]
f_1 = f[:,:,1]
f_2 = f[:,:,2]

image(g,"bbb" ,1) #display kernel
image(g_r,"bbbb", 1) #display reversed kernel

 #implement convolution for image
def conv(f):
 c = f*0
 for i in range(f.shape[0] - g_r.shape[0]):
  for j in range(f.shape[1] - g_r.shape[1]):
    c[i:i+g_r.shape[0],j:j+g_r.shape[1]]=np.multiply(f[i:i+g_r.shape[0], j:j+g_r.shape[1]], g_r)
    c[i,j]=np.sum(c[i:i+g_r.shape[0], j:j+g_r.shape[1]])
#image(conv(f_0),"nnn",1)

conv(f_0) #convolution of the first layer
conv(f_1) #convolution of the second layer
conv(f_2) #convolution of the third layer
result=np.stack((f_0,f_1,f_2),axis=2)
image(result,"result",100)
end = datetime.datetime.now() #calculate the ending time
print('Execution time is, ', end-start) #output execution time