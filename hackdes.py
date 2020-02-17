n=int(input())
x=0
for i in range(n):
    for j in range(0,n):
        print((x+i+j),end=" ")
        x+=1
    print()
