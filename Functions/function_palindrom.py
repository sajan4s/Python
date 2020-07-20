# Function to check if input is palindrome or not
# This case, not need to check the input case

def palindrom(x):
    # Remove spaces
    s = x.replace(' ','')

    # Check string with reverse of that string

    return s == s[::-1]

print(palindrom("malayalam"))