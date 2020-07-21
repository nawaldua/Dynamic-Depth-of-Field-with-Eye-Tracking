def mouse_move(event,x,y,flags, param):
    global posx, posy
    if event == cv.EVENT_MOUSEMOVE:
        posx = x
        posy = y


# Display Function
def output_win():
    global posx, posy
    posx = 0
    posy = 0
    
    outputarray = opimarr
    luptable = opluptable
    
    cv.namedWindow('output')
    
    cv.setMouseCallback('output',mouse_move)
    
    # Moving across width is x value
    # Moving along height is y value
    # table[frame_index][row or y][col or x]
    
    frame = outputarray[0][9]
    i = 0
    blur_area = 9
    comp_var = 9
    
    font = cv.FONT_HERSHEY_SIMPLEX 
    fontScale = 1
    color = (0, 0, 255)
    thickness = 2
    
#     print(len(imarr))
        
    while(i < len(imarr)):

        frame = outputarray[i][blur_area]
        cv.imshow('output',frame)        
        time.sleep(0.04)

        i += 1

        if i == len(imarr):
            i = 0

        comp_var = np.uint8(luptable[i][posy][posx])

        if comp_var < 10:
            blur_area = comp_var

        if cv.waitKey(20) & 0xFF == 27:
            break


    cv.destroyAllWindows()
    
    return

def genpreview(blurfac):
    
    global img, arr1
    img = cv.imread(dirr + '/00000.jpg')
    arr1 = np.load(dirr + '/00000.npy')
    
    global imarr
    imarr, npyarr = read_inputs()
    
    minar=np.min(npyarr[0])
    step=np.round((np.max(npyarr[0])-np.min(npyarr[0]))/10,3)

    blarrs = []
    for i in range(10):
        blarrs.append(foccal(minar+i*step, step, minar))
        
    global opims, lup_tab

    blurimages,masks, lup_tab=newmaskimg(imarr[0], npyarr[0], blurfac)
    opims=renderopfast(blurimages,blarrs,imarr[0], masks)
    return

def preview_win():
    blurfac = int(blurVariable.get())
#     print(blurVariable.get())
    genpreview(blurfac)
    
    global posx, posy
    posx = 0
    posy = 0
    
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
            
        frame = opims[blur_area]
        cv.imshow('Preview output',frame)        
#         time.sleep(0.04)
            
        comp_var = np.uint8(lup_tab[posy][posx])

        if comp_var < 10:
            blur_area = comp_var

        if cv.waitKey(20) & 0xFF == 27:
            break


    cv.destroyAllWindows()
    
    return
