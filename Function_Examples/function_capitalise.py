# Function
# Capitalise 1st and 4th letter in a string

def captilise(text):
    firt_letter = text[0]
    between = text[1:3]
    fourth_letter = text[3]
    rest= text[4:]

    return firt_letter.upper() + between + fourth_letter.upper() + rest

print(captilise("jamesbond"))