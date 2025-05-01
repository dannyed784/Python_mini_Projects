# Make a two player ROCK PAPER SCISSORS game.
import os
import random
import sys
os.system('cls' if os.name == 'nt' else 'clear')

#MY SOLUTION
try:
  user = int(input("rock = 1, paper = 2, scissors = 3: give me a number: \n"))
  if user not in [1,2,3]:
    print("Invalid number. Please choose 1, 2, or 3")
    sys.exit()
  num = random.randint(1,3)

  print(user,num)

  def rock_paper_scissors(user,num):
      if user == 1 and num == 1:
        print("rock vs rock: draw")
      elif user == 1 and num == 2:
        print("rock vs paper: you lose")    
      elif user == 2 and num == 2:
        print("paper vs paper: draw")   
      elif user == 2 and num == 3:
        print("paper vs scissors: you lose")    
      elif user == 3 and num == 3:
        print("scissors vs scissors: draw") 
      elif user == 1 and num == 3:
        print("rock vs scissors: you win") 
      elif user == 2 and num == 1:
        print("paper vs rock: you win")      
      elif user == 3 and num == 1:
        print("scissors vs rock: you lose")        
      elif user ==3 and num == 2:
        print("scissors vs paper: you win") 

  rock_paper_scissors(user,num)   
  

except ValueError:
  print("Please enter a valid number.")
  exit()