def newmaskimg(image,array, blurparam):
    
    step=np.round((np.max(array)-np.min(array))/10,3)
    minar=np.min(array)
    maxar=np.max(array)
    
    stepar=[]
    for i in range(1,12):
        #print(i)
        x=minar+(i-1)*step
#         if np.round(x)==1:
#             x==1.00
            #print(x)
#         stepar.append(np.round(x,2))
        stepar.append(x)
#     print(stepar)
    
    brack=[]
    for i in range(0,10):
        brack.append([stepar[i],stepar[i+1]])
    brack[9][1] = 1
#     print(brack)
    
    masks=[]
    temp_table = np.zeros((img.shape[0],img.shape[1]))
    for i in range(0,10):
        newarr=copy.copy(array)
        newarr[np.where(newarr>brack[i][1])]=0
        newarr[np.where(newarr<brack[i][0])]=0
        newarr[np.where(newarr>0)]=1
        #mask=np.zeros(image.shape)
        #  print(mask[:,:,0].shape)
        resized = cv.resize(newarr, (img.shape[1],img.shape[0]), interpolation = cv.INTER_AREA)
#         print(resized.shape)
#         temp_table += i*resized[:,:,0]
        temp_table += i*resized
        mask=np.dstack([resized,resized,resized])
        #print('mask',mask.shape)
        masks.append(mask)
        
    imar=[]
    for i in range(4):
        imar.append(cv.GaussianBlur(image,(blurparam*i+1,blurparam*i+1),0))
        #print(10*i+1)
        
#     print(temp_table)
    return(imar,masks, temp_table)
