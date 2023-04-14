# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:40:16 2021

@author: umeshika
"""
from skimage import io, img_as_float
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

def image(data,grid_size=5,grid="on",cmap='gray'):
    d=data
    plt.figure()
    plt.imshow(d,cmap='gray',extent=[0,d.shape[0],d.shape[1],0])
    if grid=="on":
        plt.pcolormesh(d, edgecolors='midnightblue',
                       linestyle='dotted',linewidth=1,cmap='gray')
    ax = plt.gca()
    ax.set_xticks(np.arange(0.5, d.shape[0], grid_size))
    ax.set_xticklabels((np.arange(0.5, d.shape[0], grid_size)-0.5).astype(int))
    ax.set_yticks(np.arange(0.5, d.shape[1], grid_size))
    ax.set_yticklabels((np.arange(0.5, d.shape[1], grid_size)-0.5).astype(int))
    plt.show()
#%% 
f= np.array(Image.open('archie_pix.jpg'))  
img= img_as_float(io.imread("archie_pix.jpg"))
R=img[ : , : , 0]
G=img[ : , : , 1]
B=img[ : , : , 2] 
g_k=np.array([[1/16,1/8,1/16],
              [1/8,1/4,1/8],
              [1/16,1/8,1/16]])    
g_r=np.rot90(g_k,1)
#%%
for i in range(R.shape[0]-g_r.shape[0]):
    for j in range(R.shape[1]-g_r.shape[1]):
        CR[i:i+g_r.shape[0],j:j+g_r.shape[1]]=np.multiply(R[i:i+g_r.shape[0],
                                                              j:j+g_r.shape[1]],g_r)
        CR[i,j]=np.sum(CR[i:i+g_r.shape[0],j:j+g_r.shape[1]])

#%% 