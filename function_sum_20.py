# Function
# Given 2 integers, return True if sum is 20 or if one of the interger is 20. If not, return False

def check(n1, n2):
    if n1 == 20 or n2 == 20:
        return True
    elif n1+n2 == 20:
        return True
    else:
        return False

print(check(100,10))