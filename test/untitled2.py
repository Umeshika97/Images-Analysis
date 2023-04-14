"""
Created on Thu Oct 28 09:34:55 2021

@author: umeshika
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import  color
from scipy.linalg import svd
import seaborn as sns
import os
import math

def row_matrix(A1):
    if  len(A1.shape) ==2:
        S=np.size(A1)
        #print(S) 
        B=np.reshape(A1,S)   #Taking the rows as a line
        return B
    else:
        print('error: The function support only for 2 dimentional matrices')
        return -1
        

def row_to_matrix(a,rows,columns):
    try:
        reshape = np.reshape(a,[rows,columns])
        return(reshape)
    except Exception as e:
        print(e)
        return(-1)


#%%
image_path=('E:/Third Year/Second Semester/PH 3034 Digital Image Processing 1/week 06/withoutspecs/')
files=os.listdir(image_path)
#B=np.array([])
image_data=plt.imread(image_path+files[0]);
height,width,_=image_data.shape
B=np.zeros([height*width])

for f in files:
    #print(f)
    original_img=plt.imread(image_path+f)
    original_img=color.rgb2gray(original_img)
    original_img=row_matrix(original_img)
    #B=np.append(B,original_img, axis=0)
    B=np.vstack([B,original_img])
    #np.vstack([arr,row])
B=B[1:,:]#one to the end

# %%
#U,s,VT=np.linalg.svd(B,full_matrices=False)
U,s,VT=svd(B,full_matrices=False)
print(U)
print(s)
print(VT)
plt.figure(1)
plt.plot(s,'*')
plt.title("title1")
plt.xlabel("The image")
plt.ylabel("Pixels Intesity Count")
plt.show()

plt.figure(2)
plt.semilogy(s,'*')
plt.show()

plt.figure(3)
plt.semilogy(np.diag(s),'*')
plt.title('Singular Values')
plt.show()

plt.figure(4)
plt.plot(np.cumsum(np.diag(s))/np.sum(np.diag(s)))
plt.title('Singular Values: Cumulative Sum')
plt.show()
#j=row_to_matrix(VT[0:1,:],height,width)
#plt.imshow(j,cmap='gray')

 
Variance_value = np.round(s**2/np.sum(s**2), decimals=6) 
# Variance explained top Singular vectors
print(Variance_value)
#sns.barplot(Variance_value, color="dodgerblue") 
sns.barplot(x=list(range(1, 7)),
            y=Variance_value[0:6], color="yellow")
plt.title('The Bar Graph of Variance')
plt.xlabel('The image of Singular Vector', fontsize=16)
plt.ylabel('Variance Value', fontsize=16)
#plt.tight_layout()
plt.show()


 
#%%
sum2=0
for i in range(U.shape[0]):
    for ii in files:
        truncation=6
        Re_arrange=U[i,0:truncation] @np.diag(s[0:truncation]) @VT[0:truncation,:]
        final_image=row_to_matrix(Re_arrange,height,width)
        plt.figure(i)
        plt.axis('off')#off the axis
        plt.imshow(final_image,cmap='gray')
        
        spoint1=round((final_image.shape[0])/4)
        spoint2=round((final_image.shape[0])*3/4)
        spoint3=round((final_image.shape[1])/4)
        spoint4=round((final_image.shape[1])*3/4)
        system_img=final_image[spoint1:spoint2,spoint3:spoint4]
    
        original_img=plt.imread(image_path+ii)
        ori_img=color.rgb2gray(original_img) 
        point1=round((ori_img.shape[0])/4)
        point2=round((ori_img.shape[0])*3/4)
        point3=round((ori_img.shape[1])/4)
        point4=round((ori_img.shape[1])*3/4)
        ori_img1=ori_img[point1:point2,point3:point4]
        Error=ori_img1-system_img
        SE=(Error)**2
        sum2=0
        for j in range(SE.shape[0]):
            for g in range(SE.shape[1]):
                sum2=sum2+SE[j,g]
        RMSE=math.sqrt(sum2)       
print(RMSE)

