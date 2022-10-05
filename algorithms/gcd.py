"""
This is an implementation of the Euclid's algprithm to solve the greatest common divisor problem
"""
def gcd(num1, num2):
    if num1 == 0:
        return num2
    num1, num2 = min(num1, num2), max(num1, num2)
    remainder = num2 % num1
    return gcd(remainder, num1)
    

