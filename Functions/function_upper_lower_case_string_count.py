# Function to find number of upper case and lower case characters in a string


def check(x):

    lowercase = 0
    uppercase = 0

    for i in x:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
        else:
            pass


    print(f'uppercase count: {uppercase}')
    print(f'Lowercase count: {lowercase}')


check("What is my name?")