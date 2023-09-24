#34.Sum of Digits
n=int(input("Enter the number:"))
total=0
while n>0:
    r=n%10
    total=total+r
    n=n//10
print("The sum is:",total)