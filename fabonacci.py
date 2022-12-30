# Taking input from user.
terms = int(input('Enter a number :'))

# defining variables
n1, n2 = 0, 1
count = 0
result = []

# Checking for conditions
# checking for zero
if terms <= 0:
    print('Enter a positive integer')
# cheking for 1
elif terms == 1:
    print('Fibonacci seq of 1 is =',n1)
else:
    while count < terms:
        # append n1 value to the list
        result.append(n1)
        #  sum of n1 and n2 is nth
        nth = n1+n2
        # n1 now have the value of n2
        n1 = n2
        # n2 now have the value of nth
        n2 = nth
        # increment counter by one on each iteration.
        count += 1
    print(result)
