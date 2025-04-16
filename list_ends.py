# LIST ENDS 
# Write a program that takes a list and makes a new list of only
# the first and last elements od the given list. For practice, write this code inside a function.
import os
os.system("clear")


# MY PROGRAM SOLUTION
list1 = [5,10,15,20,25]
list2 = ["peach","pear","apple",'orange','lime']

def list_ends(list):
  newlist = []
  for index, value in enumerate(list):
    if index == 0:
      newlist.append(value)
    elif index == len(list)-1:
      newlist.append(value)
  return newlist

print(list_ends(list1))
print(list_ends(list2))

#OTHER SOLUTION
def list_ends2(a_list):
  return [a_list[0], a_list[len(a_list)-1]]

print(list_ends2(list1))
print(list_ends2(list2))