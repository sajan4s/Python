# Function
# Reverse the sentence

def reverse_word(text):

    wordlist = text.split()
    reverse_word_list = wordlist[::-1]

    return ' '.join(reverse_word_list)

print(reverse_word("This is a text that needs to be reversed"))