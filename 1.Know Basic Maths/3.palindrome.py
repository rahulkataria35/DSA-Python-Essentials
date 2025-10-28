'''
Check if a given number is a palindrome or not 
Ex 151 backwards is 151 where as 123 backward is 321 

'''

def is_palindrome_number(number):
    # Convert the number to a string to check for palindrome
    str_number = str(number)
    
    # Check if the string representation of the number is the same forwards and backwards
    return str_number == str_number[::-1]

def is_palindrome_string(s):
    # Remove any spaces and convert to lowercase for uniformity
    cleaned_string = s.replace(" ", "").lower()
    
    # Check if the cleaned string is the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]


# Coding Ninja Solution

# n = int(input())
# rev =  int(str(n)[::-1])

# if (rev == n):
#     print("true")
# else:
#     print("false")


# Leetcode Solution

x = int(input())
rev = 0
nN = x
while(nN > 0):
    reminder = nN % 10
    rev = rev * 10 + reminder
    nN //= 10
if(rev == x):
    print(True)
else:
    print(False)
        
        