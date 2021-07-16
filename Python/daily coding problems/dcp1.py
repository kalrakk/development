#QUESTION1:Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#for example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].




lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input("enter the element ")) 
    lst.append(ele)
k=0

lst1=[]
while(k<n):
    ele1=1
    for j in range(0,n):
        ele1=(ele1*lst[j])
    ele1=ele1/lst[k]
    lst1.append(ele1)
    k=k+1
print(lst1)     
