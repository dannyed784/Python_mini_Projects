import os
import random
import string
os.system("clear")

print("***WELCOME TO PASSWORD GENERATOR V1.0***")

# the password needs to include:
# 2 uppercase letters from A to Z
# 2 lowercase letters from a to z
# 2 digits from 0 to 9
# 2 punctiation signs such as ! ? # etc

#Using Python you can easily access ASCII values of character using the ord() function. For
#instance ord("M") returns 77 and chr(77) returns "M".

#randint(): Returns a random number between the given range

#1.Generate 2 random uppercase letter between A to Z
uppercase_letter1 = chr(random.randint(65,90)) #first random uppercase letter  
uppercase_letter2 = chr(random.randint(65,90)) #second random uppercase letter 

#2. Generate 2 random lowercase letter between a to z
lowercase_letter1 = chr(random.randint(97,122)) #first random lowercase letter
lowercase_letter2 = chr(random.randint(97,122)) #second random lowercase letter

#3. Generate 2 random digit between 0 to 9
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))

# 4. Generate 2 random punctuation sign
punctuationSign1 = chr(random.randint(33,152))
punctuationSign2 = chr(random.randint(33,152))

#5. Generate de password 
password = (uppercase_letter1 + uppercase_letter2 + lowercase_letter1 + lowercase_letter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2)

#6. Create a list with password chartacters
password_list = list(password)
#7. Cleatn the password list for non printable characters
cleaned_password = [ch for ch in password_list if ch in string.printable]

#8. Shuffle the password cleaned list
random.shuffle(cleaned_password)

#8. join the password list
cleaned_password_result = ''.join(cleaned_password)
print(cleaned_password_result)


