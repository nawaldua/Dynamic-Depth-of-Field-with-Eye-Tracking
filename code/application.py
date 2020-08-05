import globalvars
import cv2 as cv
from iploader import read_inputs
import numpy as np
from blurproc import foccal, newmaskimg, renderopfast
from tqdm import tqdm
import os


def application():
    globalvars.img = cv.imread(globalvars.dirr + '/data/00000.jpg')
    globalvars.arr1 = np.load(globalvars.dirr + '/data/00000.npy')

    blur_factor = int(globalvars.blurVariableMain.get())

    if not globalvars.imarr:
        read_inputs()

    minar = np.min(globalvars.npyarr[0])
    step = np.round((np.max(globalvars.npyarr[0]) - np.min(globalvars.npyarr[0])) / 10, 3)

    blarrs = []
    variance = float(globalvars.blur_falloff_main.get())
    for i in range(10):
        blarrs.append(foccal(minar + i * step, step, minar, variance))

    globalvars.opimarr = []
    globalvars.opluptable = []

    for index in tqdm(range(len(globalvars.imarr)), unit="Frame(s)", desc="Processing"):

        blurimages, masks, lup_tab = newmaskimg(globalvars.imarr[index], globalvars.npyarr[index], blur_factor)

        # Per Frame image output
        opims = renderopfast(blurimages, blarrs, globalvars.imarr[index], masks)

        if not os.path.exists('outputs'):
            os.makedirs('outputs')
        for j in range(10):
            cv.imwrite("outputs/{:0>5}_{}.jpg".format(index, j), opims[j])
            np.save("outputs/{:0>5}.npy".format(index), lup_tab)

    return
