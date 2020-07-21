def read_inputs():
    #Directory 
    imarr = []    
    npyarr = []

    #Reading Image Files
    for filename in glob.glob(dirr + '/' + '*.jpg'):
        imtemp = cv.imread(filename)
        imarr.append(imtemp)

    #Reading Numpy Arrays
    for filename in glob.glob(dirr + '/' + '*.npy'):
        arrtemp = np.load(filename)
        npyarr.append(arrtemp)
        
    return imarr, npyarr
