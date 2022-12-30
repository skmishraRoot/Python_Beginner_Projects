# By using for loop
num = int(input('Enter a number :'))
result = 1
for i in range(1, num+1):
    result *= i
print(f'The factorial of {num} is = {result}') 


# By using math library from python.
import math
num = int(input('Enter a number :'))
result = math.factorial((num))
print(f'The factorial of {num} is = {result}')

