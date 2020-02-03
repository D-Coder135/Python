for i in range(0,5):
    for j in range(i+1):
        if i==3 and j==2:
            print("  ",end="")
        else:
            print("* ",end="")
    print()
