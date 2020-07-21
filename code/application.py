import globalvars
import cv2 as cv
from iploader import read_inputs
#import sys
import numpy as np
from blurproc import foccal,newmaskimg,renderopfast
from tqdm import tqdm
def application():

    globalvars.img = cv.imread(globalvars.dirr + '/(01).jpg')
    globalvars.arr1 = np.load(globalvars.dirr + '/(01).npy')  
 #   print(sys.getsizeof(globalvars.img))
  #  print(sys.getsizeof(globalvars.arr1))
    

#     start_time = time.process_time()
    globalvars.imarr, npyarr = read_inputs()
#     print("--- %s seconds ---" % (time.process_time() - start_time))
    #print(sys.getsizeof(globalvars.imarr))
   # print(sys.getsizeof(npyarr))

    minar=np.min(npyarr[0])
    step=np.round((np.max(npyarr[0])-np.min(npyarr[0]))/10,3)

    blarrs = []
    for i in range(10):
        blarrs.append(foccal(minar+i*step, step, minar))
        

    globalvars.opimarr = []
    globalvars.opluptable = []
    for index in tqdm(range(len(globalvars.imarr)), unit="Frames", desc="Processing"):

        minar=np.min(npyarr[index])
        maxar=np.max(npyarr[index])
        step=np.round((np.max(npyarr[index])-np.min(npyarr[index]))/10,3)

        blurimages,masks, lup_tab=newmaskimg(globalvars.imarr[index], npyarr[index], 6)

        #Per Frame image output
        opims=renderopfast(blurimages,blarrs,globalvars.imarr[index], masks)

        #Append opims onto the output image array
        globalvars.opimarr.append(opims)

        #Append luptable
        globalvars.opluptable.append(lup_tab)
        
    return
