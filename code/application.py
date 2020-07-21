def application():
    global img, arr1
    img = cv.imread(dirr + '/00000.jpg')
    arr1 = np.load(dirr + '/00000.npy')  
    print(sys.getsizeof(img))
    print(sys.getsizeof(arr1))
    
    global imarr
#     start_time = time.process_time()
    imarr, npyarr = read_inputs()
#     print("--- %s seconds ---" % (time.process_time() - start_time))
    print(sys.getsizeof(imarr))
    print(sys.getsizeof(npyarr))

    minar=np.min(npyarr[0])
    step=np.round((np.max(npyarr[0])-np.min(npyarr[0]))/10,3)

    blarrs = []
    for i in range(10):
        blarrs.append(foccal(minar+i*step, step, minar))
        
    global opimarr, opluptable
    opimarr = []
    opluptable = []
    for index in tqdm(range(len(imarr)), unit="Frames", desc="Processing"):

        minar=np.min(npyarr[index])
        maxar=np.max(npyarr[index])
        step=np.round((np.max(npyarr[index])-np.min(npyarr[index]))/10,3)

        blurimages,masks, lup_tab=newmaskimg(imarr[index], npyarr[index], 6)

        #Per Frame image output
        opims=renderopfast(blurimages,blarrs,imarr[index], masks)

        #Append opims onto the output image array
        opimarr.append(opims)

        #Append luptable
        opluptable.append(lup_tab)
        
    return
