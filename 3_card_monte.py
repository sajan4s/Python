#3 card monte

from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def player_guess():

    guess=' '

    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1 or 2: ")

    return int(guess)

def check_guess(my_list,guess):
    if my_list[guess]=='O':
        print("correct")
    else:
        print("Wrong guess")
        print(my_list)


# Initial list
my_list=[' ','O',' ']

# Shuffle list
mixedup_list=shuffle_list(my_list)

# User guess
guess = player_guess()

# Check guess
check_guess(mixedup_list,guess)