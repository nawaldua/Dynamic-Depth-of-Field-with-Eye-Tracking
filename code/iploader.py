import glob
import globalvars
import cv2 as cv
import numpy as np


def read_inputs():
    # Directory 
    imarr = []
    npyarr = []

    # Reading Image Files
    for filename in glob.glob(globalvars.dirr + '/' + '*.jpg'):
        imtemp = cv.imread(filename)
        imarr.append(imtemp)

    # Reading Numpy Arrays
    for filename in glob.glob(globalvars.dirr + '/' + '*.npy'):
        arrtemp = np.load(filename)
        npyarr.append(arrtemp)

    return imarr, npyarr
