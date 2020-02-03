n=int(input("Enter Number:"))
a=0
b=1
c=0
print("Fibbonacci Series upto entered n is =")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
