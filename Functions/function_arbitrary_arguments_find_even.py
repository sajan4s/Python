# Function to enter arbitrary number of arugments and return even arguments

def myfunc(*args):
    output=[]
    for n in args:
        if n%2 == 0:
            output.append(n)
    return output