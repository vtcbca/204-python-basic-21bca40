a=int(input("Enter any number:"))
b=a
rev=0
while(a!=0):
    k=a%10
    rev=rev*10+k
    a=a//10
if(b==rev):
    print("Number is pellindrom")
else:
    print("Number is not pellindrom")
