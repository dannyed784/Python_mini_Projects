#CHECK PRIMALITY FUNCTIONS
#Ask the user for a number and determine whether the number is prime or not.(prime number is 
#a number that can only be divided by 1 and itself).

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for number in range(1,21):
    if is_prime(number):
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")    
