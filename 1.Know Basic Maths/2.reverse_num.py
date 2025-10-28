
def reverse_num(n):
    # store the reverse of the input integer.
    revNum = 0
    # Start a while loop to reverse the digits of the input integer.
    while n > 0:
        # Extract the last digit of 'n' and store it in 'ld'.
        ld = n % 10
        # Multiply the current reverse number by 10 and add the last digit.
        revNum = (revNum * 10) + ld
        # Remove the last digit from 'n'.
        n = n // 10
    return revNum

# test
print(reverse_num(123))