# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 08:44:45 2021

@author: umeshika
"""
from skimage import io, img_as_float
import numpy as np
import matplotlib.pyplot as plt


#from datetime import datetime 

#%matplotlib inline

img= img_as_float(io.imread("archie_pix.jpg"))
R=img[ : , : , 0]
G=img[ : , : , 1]
B=img[ : , : , 2]
CR=R*0
CG=G*0
CB=B*0
g_k=np.array([[1/16,1/8,1/16],
              [1/8,1/4,1/8],
              [1/16,1/8,1/16]])
g_r=np.rot90(g_k,2)

A = np.array(R)
B = np.array(G)
C = np.array(B)
D = np.add(A, B, C)
#%%
for i in range(R.shape[0]-g_r.shape[0]):
    for j in range(R.shape[1]-g_r.shape[1]):
        CR[i:i+g_r.shape[0],j:j+g_r.shape[1]]=np.multiply(R[i:i+g_r.shape[0],
                                                              j:j+g_r.shape[1]],g_r)
        CR[i,j]=np.sum(CR[i:i+g_r.shape[0],j:j+g_r.shape[1]])

#%% 
plt.imshow(CR)
plt.title("dog",
          fontsize='14')
plt.show()
  
'''plt.title('R channel')
plt.imshow(R)
plt.show() 

plt.title('G channel')
plt.imshow(G)
plt.show() 

plt.title('B channel')
plt.imshow(B)
plt.show() 

plt.title('RGB channel')
plt.imshow(D)
plt.show() 
#%%
print(A)
print(B)
print(C)
print(D)'''
