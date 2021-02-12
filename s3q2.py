x = []
N = int(input('enter size of list : '))
for i in range(0, N):
    element=int(input('Enter element:'))
    x.append(element)   
print('Numbers in the list are ')
print(x)
element=int(input('enter element to be searched')) 
for i in range(0,N):
    if element==x[i]:
        found=i
        print('element found at position',found) 
    else:
        print('element not found')
