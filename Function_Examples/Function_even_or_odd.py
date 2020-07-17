# Function to find lesser for 2 numbers

def myfunc(a,b):
    if a%2 == 0 and b%2 == 0:
        #Both numbers are even
        if a < b:
            result = a
        else:
            result = b
    else:
        # One or both numbers are odd
        if a > b:
            result = a
        else:
            result = b

    return result

print(myfunc(9,4))
