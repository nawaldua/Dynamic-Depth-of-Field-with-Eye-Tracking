def renderopfast(blimg,blarray,image, masks):
    
    oparray=[]
    for j in range(10):
        recons=np.zeros(image.shape)
        for i in range(10):
            if blarray[j][i]==1:
                recons=recons+masks[i]*blimg[0]
            elif blarray[j][i]==3:
                recons=recons+masks[i]*blimg[1]
            elif blarray[j][i]==5:
                recons=recons+masks[i]*blimg[2]
            elif blarray[j][i]==7:
                recons=recons+masks[i]*blimg[3]
        
        oparray.append(recons)
        
    return(np.uint8(oparray))
