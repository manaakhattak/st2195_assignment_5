def is_divisible_by_k(x, k):
    '''
    Checks whether x us divisible by k.
    '''
    assert x%k == 0 
'''
Store all the integers that are multiples of 2 or 5 oro 7 that ar lower or equla to 1000(excluding doubles)
'''
x = ()
for i in range(1000):  
    if (is_divisible_by_k(k, 2) & is_divisible_by_k(k, 3)| is_divisible_by_k(k, 7)): 
        x.append(i)
        
        
'''
Sum all the integers that are multiples or 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''
sum(x)
'''

 
     