#date 04-16-2024
#simple game about user interaction

#display_function

game_list = [0, 1, 2]

def display_game(game_list):
    
    print("Here is the current list: ")
    print (game_list)

#display_game(game_list)

#defining a function for position choice 

def position_choice():

    choice = 'wrong'

    while choice not in ['0','1','2']:

        choice = input('Pick a position (0,1,2):  ')

        if choice not in ['0','1','2']:
            print('Sorry, invalid choice')
        
    return int(choice)

#position_choice()

#function for replacement value

def replacement_choice(game_list, position):

    user_palcement = input('Type a string to place at position: ')

    game_list[position] = user_palcement

    return game_list

#replacement_choice(game_list,1)

#function to ask the player if he wants to kee palying

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice  = input("Do you want to keep playing? Y or N: ")

        if choice not in ['Y', 'N']:
            print('Sorry I dont understand! Please choose Y or N ')

    if choice == 'Y':
        return True
    else:
        return False
    
#gameon_choice()


game_on = True
game_list = [0,1,2]

while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()


