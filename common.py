l1=list(map(int,input("Enter the list : ").split()))
l2=list(map(int,input("Enter the list : ").split()))
l3=[x for x in l1 if x in l2]
print(l3)
