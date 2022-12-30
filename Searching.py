# Its a list of number where we have values from 1 to 10,000
datatowork = [x for x in range(1,10001)]

# For finding item in a sequential list we use things like binary search. List has a inbuilt function to check our element index is list.index(target, start, end)

# Linear search
def linear_serach():
    target = int(input('Number to serach from list : '))
    for number in datatowork:
        if datatowork[number] == target:
            return number
        else:
            pass


# Binary search (only of sequnetial lists.)
def Binary_search(arr, x , low, high,):
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif x > arr[mid]:
        return Binary_search(arr, x, mid + 1, high)    
    elif x < arr[mid]:
        return Binary_search(arr, x, low, mid-1)
    else:
        return 'Not found'

     

