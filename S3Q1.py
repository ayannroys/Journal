x = []
N = int(input('enter size of list : '))
for i in range(0, N):
    element=int(input('Enter element:'))
    x.append(element)
print('Numbers in the list are ')
print(x)
max = x[0]
for i in range(0, N):
    if ( x[i] > max): 
        max = x[i]
print('Maximum value in the list = ', max)
