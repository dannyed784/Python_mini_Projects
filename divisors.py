# Create a program that ask the user for a number and then prints out 
# a list all the divisors of that number.

import os
os.system('cls' if os.name == 'nt' else 'clear')

#MY SOLUTION
user_num = int(input('Hi give me a number to know its divisors: \n'))

def divisors(number):
  num = range(2,101)
  result = []
  for n in num:
     if number % n == 0:
       result.append(f'{n} is a divisor of {number}')
  return result
    
for line in divisors(user_num):
  print(line)

#OTHER SOLUTION
num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)