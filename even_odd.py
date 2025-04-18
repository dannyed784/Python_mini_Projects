#Ask the user for a number. Depending on whether the number is even ir odd, print out an
#appropriate message to user.
import os
os.system('cls' if os.name == 'nt' else 'clear')

#MY SOLUTION
#Ask user for a number
number = int(input("Give me a number: "))

def even_or_odd(n):
    if n%2 == 0:
        print("it is an even number")
    else:
        print("it is an odd number")    

even_or_odd(number)        

#OTHER SOLUTION
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("You picked an odd number")
else:
    print("You picked en even number")    

# A MORE SOLIDE SOLUTION
def even_or_odd2(n):
    result = "even" if n % 2 == 0 else "odd"
    print(f"it is an {result} number")
even_or_odd2(number)