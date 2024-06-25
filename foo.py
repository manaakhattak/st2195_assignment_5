def is_divisible_by_k(x, k):
    '''
    Checks whether x us divisible by k.
    '''
    return x%k == 0 # using return instead of assert to return the result.
    
'''
Store all the integers that are multiples of 2 or 5 oro 7 that ar lower or equla to 1000(excluding doubles)
'''
x = [] # change to list not tuple
for i in range(1, 1001): # range needed to include 1000 
    if (is_divisible_by_k(i, 2) & is_divisible_by_k(i, 5)| is_divisible_by_k(i, 7)): # change k to i and fix the multiples 
        x.append(i)
        
        
'''
Sum all the integers that are multiples or 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''
var = sum(x) # save the variable
print(var) # print the var 