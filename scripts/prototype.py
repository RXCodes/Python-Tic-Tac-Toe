# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:44:57 2023

@author: Garrett
"""

# Defines the different ending states of the game
def ending_state(board):
    if board.position(0) == board.postion(1) == board.position(2) == 'X':
        return 'X'
    elif board.position(0) == board.postion(1) == board.position(2) == 'O':
        return 'O' 
    elif board.postion(0) != ' ':
        return 'Draw'
    else:
        return 'Continue'


# Main game program

game_state = 'Continue'
player_x = 'human'
player_o = 'human'
player = 'X'
play_again ='y'

while play_again == 'y':    
    board = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
        ]
    
    # Pre-game start set up
    # Should take inputs for human or computer players
    # And the order of players in the game
    
    # Print the blank board
    print()
    print('', board[0][0], '|', board[0][1], '|', board[0][2])
    print('--- --- ---')
    print('', board[1][0], '|', board[1][1], '|', board[1][2])
    print('--- --- ---')
    print('', board[2][0], '|', board[2][0], '|', board[2][2])
    print()
    
    
    
    while game_state == 'Continue':
        player_row = ' '
        
        while player_row == ' ':
            player_row = int(input('Which row would you like to place your piece?: '))
            player_col = int(input('Where in the row would you like to place your piece?: '))
            
            if board[player_row][player_col] == ' ':
                board[player_row][player_col] = player
            else:
                print('That space is already taken. Please enter a valid move')
                print()
                player_row = ' '
                player_col = ' '
        
        # print the board to the console
        print()
        print('', board[0][0], '|', board[0][1], '|', board[0][2])
        print('--- --- ---')
        print('', board[1][0], '|', board[1][1], '|', board[1][2])
        print('--- --- ---')
        print('', board[2][0], '|', board[2][0], '|', board[2][2])
        print()
        
        
        # check to see if the game has been won
        '''
        game_state = ending_state(board)
        '''
            
        # Change player for the next move
        if player == 'X':
            player = 'O'
        elif player == 'O':
            player = 'X'
        
        
        #this is purely to break out of the loop for testing purposes
        #it will need to be commented out for final delivery
        testing = input('break the loop? y or n: ')
        if testing == 'y':
            break
        
        
      
    
    #End of the game
    if game_state == 'Draw':
        print('The game has ended in a draw.')
        print()
    else:
        print('Player', game_state, 'has won the game.')
        print()
    
    play_again = input('would you like to play again? y or n ')
