string1='apeejay'
list1=list(string1)
print(list1)
list2=list1[::-1]
print(list2)
if(list1==list2):
    print('Palindrome')
else:
    print('not a palindrome')
