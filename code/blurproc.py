import copy
import math

import cv2 as cv
import globalvars
import numpy as np


def foccal(pt, step, minar, variance):
    stepar = []
    opar = []

    varwin = variance * step / ((2 * math.pi) ** 0.5)
    for i in range(1, 12):
        x = minar + (i - 1) * step

        stepar.append(np.round(x, 2))
        func = (1 / (((2 * math.pi) ** 0.5) * varwin)) * math.exp(-(x - pt) ** 2 / (2 * (varwin ** 2)))
        func = np.round(func, 8)
        opar.append(func)
    foclist = opar
    gpar = []

    focar = np.round(np.max(foclist) - foclist)
    for i in range(0, 10):
        gpar.append(2 * int(focar[i]) + 1)

    return gpar


def newmaskimg(image, array, blurparam):
    step = np.round((np.max(array) - np.min(array)) / 10, 3)
    minar = np.min(array)

    stepar = []
    for i in range(1, 12):
        x = minar + (i - 1) * step
        stepar.append(x)

    brack = []
    for i in range(0, 10):
        brack.append([stepar[i], stepar[i + 1]])
    brack[9][1] = 1

    masks = []
    temp_table = np.zeros((globalvars.img.shape[0], globalvars.img.shape[1]))
    for i in range(0, 10):
        newarr = copy.copy(array)
        newarr[np.where(newarr > brack[i][1])] = 0
        newarr[np.where(newarr < brack[i][0])] = 0
        newarr[np.where(newarr > 0)] = 1

        resized = cv.resize(newarr, (globalvars.img.shape[1], globalvars.img.shape[0]), interpolation=cv.INTER_AREA)

        temp_table += i * resized[:, :, 0]
        if resized.shape[2] != 3:
            mask = np.dstack([resized, resized, resized])
        else:
            mask = resized

        masks.append(mask)

    imar = []
    for i in range(4):
        imar.append(cv.GaussianBlur(image, (blurparam * i + 1, blurparam * i + 1), 0))
    return imar, masks, temp_table


def renderopfast(blimg, blarray, image, masks):
    oparray = []
    for j in range(10):
        recons = np.zeros(image.shape)
        for i in range(10):
            if blarray[j][i] == 1:
                recons = recons + masks[i] * blimg[0]
            elif blarray[j][i] == 3:
                recons = recons + masks[i] * blimg[1]
            elif blarray[j][i] == 5:
                recons = recons + masks[i] * blimg[2]
            elif blarray[j][i] == 7:
                recons = recons + masks[i] * blimg[3]

        oparray.append(recons)

    return np.uint8(oparray)
