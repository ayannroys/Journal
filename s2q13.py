
myDict = {'name': 'John', 'age': 25, 'job': 'Developer'}
print("Dictionary Items  :  ",  myDict)
key = input("Please enter the key that you want to Delete : ")
if key in myDict:
    del myDict[key]
else:
    print("Given Key is Not in this Dictionary")
print("\nUpdated Dictionary = ", myDict)

