# LIST LESS THAN TEN
import random
import os
os.system("clear")


#Generate a random number
n = random.randint(5,10)
print("Random Number: ", n)

#Generate a random list od number
def lessthan(n):
  random_list = []
  less_list =[]
  for element in range(n):
   random_list.append(random.randint(1,20))
  print("Random list generated: ",random_list) 

  for ele in random_list:
    if ele <= n:
      less_list.append(ele)
  return less_list

print(f"Execute numbers less than: {n}",lessthan(n))

