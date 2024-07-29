n=int(input("enter n:"))
temp=n
rev=0
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
if temp==rev:
    print(f"it is a {rev} palindrone number")
else:
    print("it is not a palindrone number")      
