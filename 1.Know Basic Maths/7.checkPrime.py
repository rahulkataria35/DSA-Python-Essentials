'''
Given a number, check whether it is prime or not.
A prime number is a natural number that is only divisible by 1 and by itself.
Ex: 2,3,5,7,9,11
'''

n = int(input())
count =0
'''
# brute force
for i in range (1, n+1):
    if(n%i ==0 and n %n ==0):
        count +=1
    else:
        pass
if (count ==2 or n ==1):
    print("YES")
else:
    print("NO")
    
'''
# the time complexity is O(sqrt('n')) for this code

sqrt_n = int(n**0.5)
for i in range (1, (sqrt_n+1)):
    if(n %i ==0):
        count += 1
        if(i != n //i):
            count += 1


def is_prime_number(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False
    
    # Check divisibility from 2 to the square root of the number
    # If a number is divisible by any number in this range, it's not prime
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    # If no divisors are found, the number is prime
    return True


# checking if the condition is meet or not 
if (count ==2):
    print("YES")
else:
    print("NO")            