# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one 
# line of Python that takes this list a and makes a new list that has only the even elements of this 
# list in it.

import os
os.system('cls' if os.name == 'nt' else 'clear')

#MY SOLUTION 
list_a = [1,4,5,6,2,7,9,12,45,10,34,32]

def list_even_num(my_list):
    result = []
    for el in my_list:
        if el % 2 == 0:
            result.append(el)
    return result
print(list_even_num(list_a))

# ONE-LINEAR VERSION:
def list_even(my_list):
    return[el for el in my_list if el % 2 == 0]

print(list_even(list_a))