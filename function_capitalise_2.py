# Function
# Capitalise 1st and 4th letter in a string

def captilise(text):

    first_half = text[:3]
    second_half = text[3:]

    return first_half.capitalize() + second_half.capitalize()

print(captilise("jamesbond"))