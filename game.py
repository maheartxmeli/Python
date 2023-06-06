#
# Python: 3.6.4
#
# Author: Mahea
#
# Purpose:  The Tech Academy's Python Course: Creating out first program together.
#           Demonstrating how to pass variables from function to function while producing a fuctional game.
#
#           Remember, function_name(variable) means that we pass in the variable.
#           Return variable means that we are returning the variable back to the calling function.


def start(nice=0,mean=0,name=''):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank the player for playing again.
        continue with the game.
    """
    #meaning, if we do not already have this user's name,
    #they are a new player and we need to get their name
    if name != '':
        print('\nThank you for playing again, ()!'.format(name))
    else:
        stop = True
        while stop:
            if name == '':
                name = input('\n Please enter your name :) \n>>> ').capitalize()
                if name != '':
                    print('\nAloha, ()!'.format(name))
                    print('\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean.')
                    print('but at the end of the game your fate \nWill be sealed by your actions.')
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ').lower()
        if pick == 'n':
            print('\nThe stranger walks away smiling...')
            nice = (nice +1)
            stop = False
        if pick == 'm':
            print('\nThe stranger glares at you \nmenacingly and storms off...')
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print('\n{}, your current toal: \n({}, Nice) and ({}, Mean'.format(name,nice,mean))


def score(nice, mean, name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else: # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    # substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \,Everyone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input('\nDo you want to play again? (Y/N): \n>>> ').lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print('\nAww okay, thanks for playing :\')')
            stop = False
            quit()
        else:
            print('\nEnter (Y) for "Yes" or (N) for "No": \n>>> ')


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # notice, i do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)

if __name__ == '__main__':
    start()



    