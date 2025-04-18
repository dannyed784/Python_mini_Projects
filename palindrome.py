# Ask the user for a string and print out whether this string is a palindrome or not.
# Palindrome --> is a string that reads the same fowards and backwards
import  os
os.system("clear")

string = "Anita lava la tina"
another_string = "A mama Roma le aviva el amor a mama"
more_string = "La ruta nos aporto otro paso natural"

def palindrome(string):
  string2 = string.replace(" ","").lower()
  compare = ''.join(reversed(string2))
  if string2 == compare:
    print("Your string is a palindrome!!")
  else:
    print("Your string is not a palindrome")  

palindrome(string)
palindrome(another_string)
palindrome(more_string)