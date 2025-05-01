# LIST OVERLAP COMPREHENSIONS
#Write a program that returns a list that contains only the elements that are common between
#the lists(without duplicates)
import os

os.system('cls' if os.name == 'nt' else 'clear')

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def comp(list1,list2):
   seen = set()
   return [num for num in list1 if num in list2 and not (num in seen or seen.add(num))]

print(comp(a,b))
