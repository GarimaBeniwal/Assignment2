s1=int(input("enter length 1:"))
s2=int(input("enter length 2:"))
s3=int(input("enter length 3:"))

if((s1+s2>s3)and(s2+s3>s1)and(s1+s3>s2)):
    test=True
else:
    test=False  

if(test):
    print("yes")
else:
    print("no")