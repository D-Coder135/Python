def convert(miles):
    km=1.6*miles
    print("miles converted in kms= ",end="")
    return km
miles=int(input("Enter miles to be converted: "))
kms=convert(miles)
print(kms)
