
import cv2 as cv
import numpy as np
import copy
import math
from time import sleep
import random
import glob
from tqdm import tqdm
import globalvars

def foccal(pt, step, minar):
    stepar=[]
    opar=[]
    varwin=4.5*step/((2*math.pi)**0.5)
    for i in range(1,12):
        #print(i)
        x=minar+(i-1)*step
        if np.round(x)==1:
            x==1.00
        #print(x)
        stepar.append(np.round(x,2))
        func=(1/(((2*math.pi)**0.5)*varwin))*math.exp(-(x-pt)**2/(2*(varwin**2)))
        func=np.round(func,8)
        opar.append(func)
    foclist=opar
    gpar=[]
    steplist=stepar
    brack=[]
    focar=np.round(np.max(foclist)-foclist)
    for i in range(0,10):
        gpar.append(2*int(focar[i])+1)
    return(gpar)

def newmaskimg(image,array, blurparam):
    
    step=np.round((np.max(array)-np.min(array))/10,3)
    minar=np.min(array)
    maxar=np.max(array)
    
    stepar=[]
    for i in range(1,12):
        #print(i)
        x=minar+(i-1)*step
#         if np.round(x)==1:
#             x==1.00
            #print(x)
#         stepar.append(np.round(x,2))
        stepar.append(x)
#     print(stepar)
    
    brack=[]
    for i in range(0,10):
        brack.append([stepar[i],stepar[i+1]])
    brack[9][1] = 1
#     print(brack)
    
    masks=[]
    temp_table = np.zeros((globalvars.img.shape[0],globalvars.img.shape[1]))
    for i in range(0,10):
        newarr=copy.copy(array)
        newarr[np.where(newarr>brack[i][1])]=0
        newarr[np.where(newarr<brack[i][0])]=0
        newarr[np.where(newarr>0)]=1
        #mask=np.zeros(image.shape)
        #  print(mask[:,:,0].shape)
        resized = cv.resize(newarr, (globalvars.img.shape[1],globalvars.img.shape[0]), interpolation = cv.INTER_AREA)
#         print(resized.shape)
#         temp_table += i*resized[:,:,0]
        temp_table += i*resized[:,:,0]
        if resized.shape[2]!=3:
            mask=np.dstack([resized,resized,resized])
        else:
            mask=resized    
                        #print('mask',mask.shape)
        masks.append(mask)
        
    imar=[]
    for i in range(4):
        imar.append(cv.GaussianBlur(image,(blurparam*i+1,blurparam*i+1),0))
        #print(10*i+1)
        
#     print(temp_table)
    return(imar,masks, temp_table)

def renderopfast(blimg,blarray,image, masks):
    
    oparray=[]
    for j in range(10):
        recons=np.zeros(image.shape)
        for i in range(10):
            if blarray[j][i]==1:
                recons=recons+masks[i]*blimg[0]
            elif blarray[j][i]==3:
                recons=recons+masks[i]*blimg[1]
            elif blarray[j][i]==5:
                recons=recons+masks[i]*blimg[2]
            elif blarray[j][i]==7:
                recons=recons+masks[i]*blimg[3]
        
        oparray.append(recons)
        
    return(np.uint8(oparray))
