num=list(eval((input("Enter numbers"))))
x = []
N = int(input('enter size of list : '))
for i in range(0, N):
    element=int(input('Enter element:'))
    x.append(element)
print('Numbers in the list are ')
print(x)
for i in x:
    if (i%5==0):
        print(i,'is divisable by 5 but not by 7')
    elif(i%7==0):
         print(i,'is divisable by 7 but not by 5')
