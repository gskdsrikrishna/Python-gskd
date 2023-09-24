#33.Reverse Number
n=int(input("Enter the number:"))
total=0
while n!=0:
    r=n%10
    total=total*10+r;
    n=n//10
print("The Reverse Number is:",total)