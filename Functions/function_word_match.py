# Function to match first letter of 2 words

def lettermatch_myfunc(text):
    wordlist=text.lower().split()

    if wordlist[0][0] == wordlist[1][0]:
        return True
    else:
        return False

print(lettermatch_myfunc("Sajan Sebastian"))