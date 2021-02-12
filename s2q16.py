l = eval(input("Enter the values:"))
temp=[]
for i in l:
    if i not in temp:
        temp.append(i)
l=list(temp)
print("List after removing duplicate elements:",l)

