#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
n=int(input("enter the size of array"))
for i in range(0,n):
    list1=[int(input("enter the element"))]
list2=[]
for i in range (0,n-1):
    ele=list1[i]+list1[i+1]
    list2.append(ele)
for i in range(0,n):
    if(k==list2[i]):
                 print(TRUE)
                 
    

        
