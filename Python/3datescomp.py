(d1,m1,y1)=(int(input("enter the first date for comparison"),int(input("date's month")),int(input("date's year")))
(d2,m2,y2)=(int(input("enter the second date for comparison"),int(input("date's month")),int(input("date's year")))
(d3,m3,y3)=(int(input("enter the third date for comparison"),int(input("date's month ")),int(input("date's year")))
if((d1,m1,y1)>(d2,m2,y2)and(d2,m2,y2)>(d3,m3,y3)):
    print("the date",d1,"/",m1,"/",y1,"is greatest of all")
elif((d2,m2,y2)>(d1,m1,y1) and (d1,m1,y1)>(d3,m3,y3)):               
    print("the date",d2,"/",m2,"/",y2,"is greatest of all")
else:
    print("the date",d3,"/",m3,"/",y3,"is greatest of all")

