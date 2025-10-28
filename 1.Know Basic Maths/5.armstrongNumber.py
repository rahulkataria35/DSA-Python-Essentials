'''
Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is equal to a given number.

Ex : 153 is 1^3 + 5^3 + 3^3 = 153

'''

n = int(input("Enter a number: "))
count = len(str(n))
# Initialize a variable to store the sum of digits raised to the power of count
arm = 0
# Store the original number in a new variable for comparison later
newN = n

# Loop through each digit of the number
while n != 0:
    # Extract the last digit of the number
    digit = n % 10
    # Add the digit raised to the power of count to the arm variable
    arm += (digit ** count)
    # Remove the last digit from the number (integer division by 10)
    n //= 10

# Check if the calculated sum of powers is equal to the original number
if newN == arm:
    print("true")  # If equal, it is an Armstrong number
else:
    print("false") # If not equal, it is not an Armstrong number
# Test Run 




def is_armstrong_number(number):
    # Convert the number to a string to easily iterate over digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of digits raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number


def is_armstrong_num(num):
    count = len(str(num))
    arm_sum = 0
    new_num = num

    while num != 0:
        digit = num % 10
        arm_sum += (digit ** count)
        num = num // 10
    
    return new_num == arm_sum


# test
print(is_armstrong_num(153))



# Example usage
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
