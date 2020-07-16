# Function to output string even letters upper and odd letters lower

def myfunc(x):
    out = []
    for n in range(len(x)):
        if n%2==0:
            out.append(x[n].lower())
        else:
            out.append(x[n].upper())
    return ''.join(out)
