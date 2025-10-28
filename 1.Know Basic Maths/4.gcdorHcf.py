'''
GCD : Greatest Common Divisor // HCF: Highest Common Divisor 

Ex :GDC or HCF of 12 and 9 is 3
 
'''

n = int(input())
m = int(input())
gcd =1

for i in range (1,min(n,m)+1):
    if(n % i == 0 and m % i == 0):
        gcd = i
print(gcd)


"""
GCD:
-----
Approach 1: Euclidean Algorithm (Iterative)
The Euclidean algorithm is a classic method for finding the GCD and is based on the principle that the GCD of two numbers also divides their difference.
"""
def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
print(gcd_iterative(48, 18))  # Output: 6

# Approach 2: Euclidean Algorithm (Recursive)
# The recursive version of the Euclidean algorithm is straightforward and elegant.
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

# Example usage
print(gcd_recursive(48, 18))  # Output: 6



"""
LCM (Least Common Multiple) Approach
The LCM of two numbers can be found using the relationship between GCD and LCM:
"""

def lcm(a, b):
    # Calculate LCM using the GCD
    return abs(a * b) // gcd_iterative(a, b)

# Example usage
print(lcm(48, 18))  # Output: 144