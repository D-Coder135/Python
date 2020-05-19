def isLeapYear(y):
    if ((y%4)==0):
        if ((y%100)==0):
            if ((y%400)==0):
                 flag=True
            else:
                flag=False
        else:
             flag=True
    else:
         flag=False
    if (flag==True):
        return True
    else:
        return False

y=int(input("Enter the year:"))
if(isLeapYear(y)==True):
    print("year is leap year")
else:
    print("year is not leap year")


                
