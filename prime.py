n=int(input("enter the value"))
i=2
while i<n:
  if n%i==0:
    print("not prime")
    break
  i=i+1
else:
  print("prime")
