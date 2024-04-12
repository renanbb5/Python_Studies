#date 04-11-24
#function to get input values and compare with some conditions
import os


def clear():
    os.system( 'clear' )

def user_choice():

    #seting a value to compare
    choice = 'not_value'

    #while the choice is not a digit , keep asking for input
    while choice.isdigit() == False:
        
        choice = input('\nPlease enter a value: ')
        clear()
    #error message check
        if choice.isdigit() == False:
            print('Sorry, but you did not enter an integer. Plesae try again')

    return print(int(choice))
   

user_choice()
