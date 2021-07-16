list1=[x for x in input("enter the elements of the list").split()]
set1=set(list1)
print(list1)
print([[i,list1.count(i)] for i in set1(list1)])
for j in list1 :
    if j not in set1 :
        set1.append(j)

print ("actual no. of elements in the list",len(set1))
        
