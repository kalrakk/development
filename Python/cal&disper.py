s1=int(input("enter marks of 1st subject"))
s2=int(input("enter marks of 2nd subject"))
s3=int(input("enter marks of 3rd subject"))
s4=int(input("enter marks of 4th subject"))
s5=int(input("enter marks of 5th subject"))
totalmarks=500
percentage=((s1+s2+s3+s4+s5)/500)*100
if(percentage<70 and percentage>60):
    print("This student is passed with first division with:",percentage,"%")
elif(percentage<80 and percentage>70):
    print("This student is passed with second division with:",percentage,"%")
elif(percentage<90 and percentage>80):
    print("This student is passed with third division with:",percentage,"%")
elif(percentage<100 and percentage>90):
    print("This student is passed with:",percentage,"%")
else:
    print("This student gor failed with:",percentage,"%")
    
