#FIBONACCI
import os
os.system("clear")


def fibonacci(n):
    a = 0
    b = 1
    for num in range(n):
       print(b)
       c = a + b
       a = b
       b = c 
        
fibonacci(10)        