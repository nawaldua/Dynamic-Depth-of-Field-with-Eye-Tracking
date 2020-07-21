import cv2 as cv
import globalvars
import numpy as np
from iploader import read_inputs
from blurproc import foccal,newmaskimg,renderopfast
import time
def mouse_move(event,x,y,flags, param):
    
    if event == cv.EVENT_MOUSEMOVE:
        globalvars.posx = x
        globalvars.posy = y


# Display Function
def output_win():
    globalvars.posx = 0
    globalvars.posy = 0
    
    
    cv.namedWindow('output')
    
    cv.setMouseCallback('output',mouse_move)
    
    # Moving across width is x value
    # Moving along height is y value
    # table[frame_index][row or y][col or x]
    
    frame = globalvars.opimarr[0][9]
    i = 0
    blur_area = 9
    comp_var = 9
    
    font = cv.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0, 0, 255)
    thickness = 2
    
#     print(len(globalvars.imarr))
        
    while(i < len(globalvars.imarr)):

        frame = globalvars.opimarr[i][blur_area]
        cv.imshow('output',frame)        
        time.sleep(0.04)

        i += 1

        if i == len(globalvars.imarr):
            i = 0

        comp_var = np.uint8(globalvars.opluptable[i][globalvars.posy][globalvars.posx])

        if comp_var < 10:
            blur_area = comp_var

        if cv.waitKey(20) & 0xFF == 27:
            break


    cv.destroyAllWindows()
    
    return

def genpreview(blurfac):
    
    
    globalvars.img = cv.imread(globalvars.dirr + '/(01).jpg')
    globalvars.arr1 = np.load(globalvars.dirr + '/(01).npy')
    
    
    globalvars.imarr, npyarr = read_inputs()
    
    minar=np.min(npyarr[0])
    step=np.round((np.max(npyarr[0])-np.min(npyarr[0]))/10,3)

    blarrs = []
    for i in range(10):
        blarrs.append(foccal(minar+i*step, step, minar))
        
    

    blurimages,masks, globalvars.lup_tab=newmaskimg(globalvars.imarr[0], npyarr[0], blurfac)
    globalvars.opims=renderopfast(blurimages,blarrs,globalvars.imarr[0], masks)
    return

def preview_win():
    blurfac = int(globalvars.blurVariable.get())
#     print(blurVariable.get())
    genpreview(blurfac)
    
    
    globalvars.posx = 0
    globalvars.posy = 0
    
    cv.namedWindow('Preview output')
    #cv.resizeWindow('output', 600,600)
    
    cv.setMouseCallback('Preview output',mouse_move)
    
    # Moving across width is x value
    # Moving along height is y value
    # table[frame_index][row or y][col or x]
    i=0
    blur_area = 9
    comp_var = 9
    font = cv.FONT_HERSHEY_SIMPLEX 
    fontScale = 1
    color = (0, 0, 255)
    thickness = 2
    
    while(i == 0):
            
        frame = globalvars.opims[blur_area]
        cv.imshow('Preview output',frame)        
#         time.sleep(0.04)
            
        comp_var = np.uint8(globalvars.lup_tab[globalvars.posy][globalvars.posx])

        if comp_var < 10:
            blur_area = comp_var

        if cv.waitKey(20) & 0xFF == 27:
            break


    cv.destroyAllWindows()
    
    return
