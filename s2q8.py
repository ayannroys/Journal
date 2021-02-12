test_list = [{'a' :  1, 'b' : 2 },  
             {'a' :  3, 'b' : 4 }] 

print("The original list is : " + str(test_list)) 

new_key = 'c'
  
add_list = [5, 6] 
  
res = [] 
for key, val in zip(test_list, add_list): 
    key[new_key] = val 
    res.append(key)   
print("The modified dictionary : " ,res)
