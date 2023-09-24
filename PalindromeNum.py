#37.Palindrome Number
n=int(input("Enter the number:"))
temp=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if temp==rev:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")