# Create a program that ask the user to enter their name and their age.
# Print out a message addressed to them that tells the year that they will turn 100 years old.

import os
os.system("clear")

#MY SOLUTION
#ask the questions to the user
name = input("What is your name?\n")
age = int(input("How old are you?\n"))

def turnTo100(name,age):
  years_= 2025 - age + 100
  return f'Hi {name} you will be 100 years old in {years_}'
print(turnTo100(name,age))

#ANOTHER SOLUTION
name1 = input("What is your name: ")
age = int(input("How old are you: "))
year = 2025 - age + 100
print(name + ", you will be 100 years old in the year " + str(year))