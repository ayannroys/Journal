num = input("Enter any number: ") 
numberNames = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
result = ''
for ch in num:
    key = int(ch) #converts character to integer
    value = numberNames[key]
    result = result + ' ' + value
print("The number is:",num)
print("The numberName is:",result)
