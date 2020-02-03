n=int(input("Enter the number:"))
l=len(str(n))
num=n
s=0
while num!=0:
    r=num%10
    s=s+(r**l)
    num=num//10
if s==n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
