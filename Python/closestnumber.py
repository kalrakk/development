list1=[int(x) for x in input("enter the numbers in list").split()]
y=int(input("enter any no. to find the closest number"))
for i in list1 :
    if(y==list1[i]):
        print("no. found")
    elif(y<list1[i]) :
        z1=list1[i]-y
        z2=list1[i+1]-y
        while(z2<z1) :
            n=z2
        print("the no. is ",n)  
            
