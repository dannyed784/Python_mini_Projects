#REVERSE WORD ORDER
import os
import stringprep
os.system("clear")

# teststring = "Daniel Moreno"
# result = teststring.split("e")
# print(result)

# joinresult = "".join(result)
# print(joinresult)

# joinresult = "e".join(result)
# print(joinresult)

# joinresult = "*".join(result)
# print(joinresult)

# listexample = ['D','a','n','i','e','l']
# joinlist = ''.join(listexample)
# print(joinlist)

# MY CODE SOLUTION

# Step1: Split the string
def reverse_string(string):
  split_string = string.split(' ')
# Step2: shift the list elements position
  split_string.reverse()
# Step3: Join the list elements 
  return ' '.join(split_string)
print(reverse_string("Daniel is a programmer")) 

# MY SECOND SOLUTION
def reverse_string2(string):
    return ' '.join(reversed(string.split(' ')))
  
print(reverse_string2("Daniel is not a doctor"))

#ANOTHER SOLUTIONS
# 1.
def reverse_v1(x):
    y = x.split()
    result = []
    for word in y:
        result.insert(0,word)
    return " ".join(result)

print(reverse_v1("Hello my friend"))

#.2
def reverse_v2(x):
    y = x.split()
    return " ".join(y[::-1])

print(reverse_v2("Rock my world!!"))

#.3
def reverse_v3(x):
    y = x.split(' ')
    return ' '.join(reversed(y))



