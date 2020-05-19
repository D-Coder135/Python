l=list(map(int,input("Enter the Elements in the set: ").split(" ")))
e=int(input("Enter the element to remove:")) 
s=set(l)
if e in s:
    s.remove(e)
    print(s)
else:
    print("Element not found in the set")
