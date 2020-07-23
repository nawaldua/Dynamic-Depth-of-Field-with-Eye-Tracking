import cv2 as cv
import globalvars
import numpy as np
from iploader import read_inputs
from blurproc import foccal, newmaskimg, renderopfast
import time


# Function to capture mouse move event in OpenCV output
def mouse_move(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEMOVE:
        # Getting x and y coordinates
        globalvars.posx = x
        globalvars.posy = y


# Main Display Function for output video
def output_win():
    # Initializing x and y mouse coordinates on output window
    globalvars.posx = 0
    globalvars.posy = 0

    # Declaring the output window
    cv.namedWindow('output')

    # Function call for checking if mouse is moved
    # Moving across width is x value
    # Moving along height is y value
    # table[frame_index][row or y][col or x]
    cv.setMouseCallback('output', mouse_move)

    # Initializing frame variables
    i = 0
    blur_area = 9

    # Continuous looping across all frames
    while (i < len(globalvars.imarr)):
        # Update frame
        frame = globalvars.opimarr[i][blur_area]
        cv.imshow('output', frame)

        # Restrict output to 25 fps
        time.sleep(0.04)

        # Increment frame counter
        i += 1

        # Facilitate looping of video
        if i == len(globalvars.imarr):
            i = 0

        # Compensate for outlier values generated during mask generation
        comp_var = np.uint8(globalvars.opluptable[i][globalvars.posy][globalvars.posx])
        if comp_var < 10:
            blur_area = comp_var

        # Keyboard input to close window with the 'ESC' key
        if cv.waitKey(20) & 0xFF == 27:
            break

    cv.destroyAllWindows()

    return


# Code to generate data for the Preview function
def genpreview(blurfac):
    # Initialize with the data for the first frame
    globalvars.img = cv.imread(globalvars.dirr + '/(01).jpg')
    globalvars.arr1 = np.load(globalvars.dirr + '/(01).npy')

    globalvars.imarr, npyarr = read_inputs()

    # Calculate the minimum and step size
    minar = np.min(npyarr[0])
    step = np.round((np.max(npyarr[0]) - np.min(npyarr[0])) / 10, 3)

    # Initialize and generate user requested blur levels(blurfac) for each of the 10 depth zones
    blarrs = []
    for i in range(10):
        blarrs.append(foccal(minar + i * step, step, minar))

    blurimages, masks, globalvars.lup_tab = newmaskimg(globalvars.imarr[0], npyarr[0], blurfac)
    globalvars.opims = renderopfast(blurimages, blarrs, globalvars.imarr[0], masks)
    return

# Display function for the Preview function
def preview_win():
    # Obtain user required blur level from the drop-down menu
    blurfac = int(globalvars.blurVariable.get())
    # Generate the requested blur level for each of the 10 depth zones
    genpreview(blurfac)
    # Initialize mouse pointer positions
    globalvars.posx = 0
    globalvars.posy = 0
    # Declaring the Output Window
    cv.namedWindow('Preview output')
    # Function call for checking if mouse is moved
    # Moving across width is x value
    # Moving along height is y value
    # table[frame_index][row or y][col or x]
    cv.setMouseCallback('Preview output', mouse_move)

    # Initializing frame variables
    i = 0
    blur_area = 9
    # Infinte loop prevents Output window from freezing while waiting for mouse move
    while (i == 0):
        # Update frame
        frame = globalvars.opims[blur_area]
        cv.imshow('Preview output', frame)
        # Compensate for outlier values generated during mask generation
        comp_var = np.uint8(globalvars.lup_tab[globalvars.posy][globalvars.posx])
        if comp_var < 10:
            blur_area = comp_var
        # Exit conditions, waiting fro 'ESC' key press
        if cv.waitKey(20) & 0xFF == 27:
            break

    cv.destroyAllWindows()

    return
