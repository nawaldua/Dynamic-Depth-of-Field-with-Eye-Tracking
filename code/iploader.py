import glob
import globalvars
import cv2 as cv
import numpy as np


def read_inputs():

    # Reading Image Files
    for filename in glob.glob(globalvars.dirr + '/data/' + '*.jpg'):
        imtemp = cv.imread(filename)
        globalvars.imarr.append(imtemp)

    # Reading Numpy Arrays
    for filename in glob.glob(globalvars.dirr + '/data/' + '*.npy'):
        arrtemp = np.load(filename)
        globalvars.npyarr.append(arrtemp)
