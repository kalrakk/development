list1=[]
num=int(input("enter any decimal value to be converted into binary"))
while(num!=0) :
    a=int(num%2)
    list1.append(a)
    num=int(num/2)
print(list1[ : :-1])
    
