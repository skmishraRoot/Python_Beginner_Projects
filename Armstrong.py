# What is armstrong number: Basically it's a number when sum of cubes of all the digits in a number equals to the number.

# First method
def is_armstrong():
    num = int(input("Enter a number: "))
    #  here we are converting a string into value then spliting into number and then converting it into integers.
    parts = [int(_) for _ in str(num)]

    sum_of_all = 0
    for _ in parts:
        sum_of_all += _**3
    return (sum_of_all == num)


# Second method
def is_armstrong_2():

    # take input from the user
    num = int(input("Enter a number: "))

    # initialize sum
    sum = 0
    # finding sum of cube of each
    temp = num
    # using a while loopg to 
    while temp > 0:
        # to get the remainder by dividing 10 we always get the last value as remainder
        # like we do 153/10 we get 3 as remainder then we do 15/10 we get 5.
        digit = temp % 10
        # calculating cube of the number and adding it to sum.
        sum += digit ** 3
        # We are performing a integer division so don't get any values with decimal by using integer division with 10 we split the last value from original number. 
        # like we do 153/10 and we get 15 then 15/10 we get 1.
        temp //= 10

    return (sum == num)


print(is_armstrong_2())