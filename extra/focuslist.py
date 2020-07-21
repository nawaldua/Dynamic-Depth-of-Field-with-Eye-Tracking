def foccal(pt, step, minar):
    stepar=[]
    opar=[]
    varwin=4.5*step/((2*math.pi)**0.5)
    for i in range(1,12):
        #print(i)
        x=minar+(i-1)*step
        if np.round(x)==1:
            x==1.00
        #print(x)
        stepar.append(np.round(x,2))
        func=(1/(((2*math.pi)**0.5)*varwin))*math.exp(-(x-pt)**2/(2*(varwin**2)))
        func=np.round(func,8)
        opar.append(func)
    foclist=opar
    gpar=[]
    steplist=stepar
    brack=[]
    focar=np.round(np.max(foclist)-foclist)
    for i in range(0,10):
        gpar.append(2*int(focar[i])+1)
    return(gpar)
