def possible(nb1,nb2,size) :
    x=size%5
    if(size>5 and nb1>=(size/5)and (x<=nb2)):
        return print("yes it is possible")
    elif(size<5) :
        if(size<=nb2) :
            return print("yes it is possible")
    else :
        return print("no it is not possible")

    


    
    
    
