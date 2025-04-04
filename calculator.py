import os
os.system("clear")

try:
#get the numbers
  num1 = int(input("Digit the first number: "))
  print(num1)
  num2 = int(input("Digit the second number: "))
  print(num2)
  oper = input("What kind of operation you want to do(+,-,*,/): ")
  print(oper)

  if oper == "+":
    result = num1 + num2
  elif oper == "-":
    result = num1 - num2    
  elif oper == "*":
    result = num1 * num2
  elif oper == "/":
    result = num1/num2       
  else:
    print("An incorrect arithmetic symbol was inserted")    

  print(f"= {result}")
except ZeroDivisionError:
  print("You can't divide by zero!")
except ValueError:
  print("Enter only numbers please!")    
except Exception:
  print("Something went wrong!")  
finally:
  print("Exit code")  