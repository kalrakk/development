ch=int(input("enter the choice\n1.add\n2.subtract\n3.divide\n4.multiply"))
a=float(input("enter the first number"))
b=float(input("enter the second number"))
if (ch==1) :
    c=a+b
    print("the sum of two numbers is ",c)
elif(ch==2) :
    c=a-b
    print("the difference two numbers is ",c)
elif(ch==3) :
    c=a/b
    print("the quotient is",c)
else :
    c=a*b
    print("the product of two numbers is ",c)
input()    
    
