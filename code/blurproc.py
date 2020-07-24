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
    stepar = []                                         #array for steps from minimum depth to maximum depth
    foclist = []                                        #Gaussian curve values
    varwin = 4.5 * step / ((2 * math.pi) ** 0.5)        #Variance
    for i in range(1, 12):
        x = minar + (i - 1) * step
        stepar.append(np.round(x, 2))
        func = (1 / (((2 * math.pi) ** 0.5) * varwin)) * math.exp(-(x - pt) ** 2 / (2 * (varwin ** 2)))
        func = np.round(func, 8)                        
        foclist.append(func)
    gpar = []                                           #inputs to the Gaussian operator

    focar = np.round(np.max(foclist) - foclist)         #Flipping the Gaussian curve upside down so that there is no blur at the center
    for i in range(0, 10):
        gpar.append(2 * int(focar[i]) + 1)              #Generating odd numbered array since Guassian does not accept even
    return (gpar)


def newmaskimg(image, array, blurparam):
    step = np.round((np.max(array) - np.min(array)) / 10, 3)
    minar = np.min(array)


    stepar = []
    for i in range(1, 12):
        x = minar + (i - 1) * step
        stepar.append(x)


    brack = []                                          #Brackets of depth within which the depth map is segmented. For instance 1<1.5<2 would place 1.5 in the first bracket.
    for i in range(0, 10):
        brack.append([stepar[i], stepar[i + 1]])
    brack[9][1] = 1

    masks = []                                          #Masks generated to separate the image into depth levels
    temp_table = np.zeros((globalvars.img.shape[0], globalvars.img.shape[1]))
    for i in range(0, 10):
        newarr = copy.copy(array)
        newarr[np.where(newarr > brack[i][1])] = 0
        newarr[np.where(newarr < brack[i][0])] = 0
        newarr[np.where(newarr > 0)] = 1                #Set values inside bracket range to 1 for mask generation
        
        resized = cv.resize(newarr, (globalvars.img.shape[1], globalvars.img.shape[0]), interpolation=cv.INTER_AREA)    #Rescaling

        temp_table += i * resized[:, :, 0]              #An array with each "pixel" containing it's corresponding depth level
        if resized.shape[2] != 3:
            mask = np.dstack([resized, resized, resized])
        else:
            mask = resized

        masks.append(mask)

    imar = []                                           #An array of four images at the required blur levels
    for i in range(4):
        imar.append(cv.GaussianBlur(image, (blurparam * i + 1, blurparam * i + 1), 0))

    return (imar, masks, temp_table)


def renderopfast(blimg, blarray, image, masks):
    oparray = []                                        #Output image generated using blurred images and the masks
    for j in range(10):
        recons = np.zeros(image.shape)
        for i in range(10):                             #Reconstruct image by multiplying blurred images by masks.
            if blarray[j][i] == 1:
                recons = recons + masks[i] * blimg[0]
            elif blarray[j][i] == 3:
                recons = recons + masks[i] * blimg[1]
            elif blarray[j][i] == 5:
                recons = recons + masks[i] * blimg[2]
            elif blarray[j][i] == 7:
                recons = recons + masks[i] * blimg[3]

        oparray.append(recons)                          #Output reconstructed image array for all possible focus levels

    return (np.uint8(oparray))
