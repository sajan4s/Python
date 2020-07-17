# Function to find lesser for 2 numbers

def myfunc(a,b):
    if a%2 == 0 and b%2 == 0:
        #Both numbers are even
        return min(a,b)
    else:
        # One or both numbers are odd
        return max(a,b)

print(myfunc(9,4))