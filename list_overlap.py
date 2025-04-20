# Take two list, say for example these two:
# and write a program that returns a list that contains only the elements that are common
# between the lists(without duplicates).Make sure your program works on two list of different sizes.

import os
os.system('cls' if os.name == 'nt' else 'clear')

#MY SOLUTION
list1 = [1,3,5,7,8,4,3,4,5,9,8,4,3]
list2 = [1,1,6,7,4,4,3,4,5,5,8,3,1,6,3,4,6]

def list_overlap(list1,list2):
    result = []
    for elem in list1:
      if elem in list2 and elem not in result:
         result.append(elem)
    return result

print(list_overlap(list1,list2))

