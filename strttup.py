s=input("Enter the String: ")
l=len(s)
a=()
b=()
c=()
for i in range(l):
    if (ord(s[i])>=97):
        a=a+tuple(s[i])
    elif (ord(s[i])>=48 and ord(s[i])<=57):
        b=b+tuple(s[i])
    else:
        c=c+tuple(s[i])
print(a)
print(b)
print(c)
    
