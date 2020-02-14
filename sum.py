n=int(input("Enter the number: "))
l1=list(map(int,input("Enter the list : ").split()))
length=len(l1)
c=0
for i in range(length):
    for j in range(i+1,length):
        if (l1[i]+l1[j])==n:
            c+=1
            break   
if c!=0:
    print("Yes")
else:
    print("No")
