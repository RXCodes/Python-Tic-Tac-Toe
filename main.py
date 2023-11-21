import simplegui
import random

# Load images
imageRootSource = "https://raw.githubusercontent.com/RXCodes/Python-Tic-Tac-Toe/main/images/"
playerOImg = simplegui.load_image(imageRootSource + "Player-O.PNG")
playerXImg = simplegui.load_image(imageRootSource + "Player-X.PNG")
background = simplegui.load_image(imageRootSource + "Tic-Tac-Toe_Blank.png")
TicTacToeMainMenu = simplegui.load_image(imageRootSource + "Tic-Tac-Toe_Main_Menu_No_Buttins.png")
TicTacToeMainCredits = simplegui.load_image(imageRootSource + "Tic-Tac-Toe_Credits.png")
TicTacToeOptions = simplegui.load_image(imageRootSource + "Tic-Tac-Toe_Options_Text.png")
backArrow = simplegui.load_image(imageRootSource + "BackArrow.PNG")
CPUHardHighlight = simplegui.load_image(imageRootSource + "CPU_Hard_Highlight.png")
CPUEasyHighlight = simplegui.load_image(imageRootSource + "CPU_Easy_Highlight.png")
Player1HumanHighlight = simplegui.load_image(imageRootSource + "Player_1_Human_Highlight.png")
Player2HumanHighlight = simplegui.load_image(imageRootSource + "Player_2_Human_Highlight.png")
Player1CPUHighlight = simplegui.load_image(imageRootSource + "Player_1_CPU_Highlight.png")
Player2CPUHighlight = simplegui.load_image(imageRootSource + "Player_2_CPU_Highlight.png")
boardImage = simplegui.load_image(imageRootSource + "Board.png")
endscreenX = simplegui.load_image(imageRootSource + "EndScreenX.png")
endscreenO = simplegui.load_image(imageRootSource + "EndScreenO.png")
endscreenTie = simplegui.load_image(imageRootSource + "EndScreenTie.png")

# Some graphical settings
gridSize = 30
iconSize = 55

def resetButtonPressed():
    goToMenu("Main Menu")

# Changes the menu
currentMenu = "Main Menu"
def goToMenu(name):
    global frame
    global currentMenu
    currentMenu = name
    if name == "Main Menu":
        global mainMenu
        frame.set_draw_handler(mainMenu)
    if name == "Board Menu":
        global boardMenu
        frame.set_draw_handler(boardMenu)
    if name == "Credits Menu":
        global creditsMenu
        frame.set_draw_handler(creditsMenu)
    if name == "Options Menu":
        global optionsMenu
        frame.set_draw_handler(optionsMenu)


# Check if point is inside rectangle
def rectangleCheck(position, rectPosition, rectSize):
    rectX = rectPosition[0] - (rectSize[0] / 2.0)
    rectX2 = rectPosition[0] + (rectSize[0] / 2.0)
    rectY = rectPosition[1] - (rectSize[1] / 2.0)
    rectY2 = rectPosition[1] + (rectSize[1] / 2.0)
    if position[0] >= rectX and position[0] <= rectX2:
        if position[1] >= rectY and position[1] <= rectY2:
            return True
    return False
        
# Handle mouse clicks
def mouse_handler(position):
    print(position)
    
    # when in the main menu (title screen)
    if currentMenu == "Main Menu":
    
        # when click on "Play Game" button
        if rectangleCheck(position, (135, 244.5), (190, 29)):
            goToMenu("Board Menu")
            startGame()
            return
            
        # when click on "Options" button
        if rectangleCheck(position, (135, 214.5), (190, 29)):
            goToMenu("Options Menu")
            return
        
        # when click on "Credits" button
        if rectangleCheck(position, (135, 184.5), (190, 29)):
            goToMenu("Credits Menu")
            return
                 
    # tapping back button will go to menu
    if currentMenu != "Main Menu":
        if rectangleCheck(position, (20, 280), (30, 30)):
            goToMenu("Main Menu")
            return
            
    # when in the game board
    if currentMenu == "Board Menu":
        
        # if in game over state, restart game
        if game_state == "end":
            startGame()
            return
        
        # check if pressed any of the slots
        doubleGridSize = gridSize * 2
        topLeftPosition = (150 - doubleGridSize, 150 - doubleGridSize)
        for row in range(3):
            for column in range(3):
                cellPosition = (
                    topLeftPosition[0] + (row * doubleGridSize),
                    topLeftPosition[1] + (column * doubleGridSize)
                )
                if rectangleCheck(position, cellPosition, (doubleGridSize, doubleGridSize)):
                    gridClicked(row, column)
                    return
                
    # when in options menu
    if currentMenu == "Options Menu":
        global player_x
        global player_o
        global hardCPUDifficulty
        
        # when tapped on "Human" for Player 1
        if rectangleCheck(position, (50.5, 150), (79, 26)):
            player_x = "player"
            return
        
        # when tapped on "CPU" for Player 1
        if rectangleCheck(position, (117.5, 150), (49, 26)):
            player_x = "bot"
            return
        
        # when tapped on "Human" for Player 2
        if rectangleCheck(position, (200.5, 150), (79, 26)):
            player_o = "player"
            return
        
        # when tapped on "CPU" for Player 2
        if rectangleCheck(position, (267.5, 150), (49, 26)):
            player_o = "bot"
            return
        
        # when tapped on "Easy" CPU difficulty
        if rectangleCheck(position, (104.5, 252.5), (55, 27)):
            hardCPUDifficulty = False
            return
        
        # when tapped on "Hard" CPU difficulty
        if rectangleCheck(position, (197.5, 252.5), (55, 27)):
            hardCPUDifficulty = True
            return
                
# draw the image to fill the entire screen
def drawToEntireScreen(canvas, image):
    if image.get_width() == 0:
        return # image is not loaded yet
    imageSize = (image.get_width(), image.get_height())
    imageCenter = (image.get_width() / 2.0, image.get_height() / 2.0)
    canvas.draw_image(image, imageCenter, imageSize, (150, 150), (300, 300))
    
# draws the back arrow
def drawBackArrow(canvas):
    if backArrow.get_width() == 0:
        return # image is not loaded yet
    imageSize = (backArrow.get_width(), backArrow.get_height())
    imageCenter = (backArrow.get_width() / 2.0, backArrow.get_height() / 2.0)
    canvas.draw_image(backArrow, imageCenter, imageSize, (20, 280), (30, 30))

# Handler to draw menus
def mainMenu(canvas):
    drawToEntireScreen(canvas, TicTacToeMainMenu)

def creditsMenu(canvas):
    drawToEntireScreen(canvas, TicTacToeMainCredits)
    drawBackArrow(canvas)
   
def optionsMenu(canvas):
    drawToEntireScreen(canvas, background)
    
    # highlight player 1 (X) option
    global player_x
    if player_x == "bot":
        drawToEntireScreen(canvas, Player1CPUHighlight)
    else:
        drawToEntireScreen(canvas, Player1HumanHighlight)
    
    # highlight player 2 (O) option
    global player_o
    if player_o == "bot":
        drawToEntireScreen(canvas, Player2CPUHighlight)
    else:
        drawToEntireScreen(canvas, Player2HumanHighlight) 
        
    # highlight difficulty option
    global hardCPUDifficulty
    if hardCPUDifficulty:
        drawToEntireScreen(canvas, CPUHardHighlight)
    else:
        drawToEntireScreen(canvas, CPUEasyHighlight)    
    
    drawToEntireScreen(canvas, TicTacToeOptions)
    drawBackArrow(canvas)
    
def boardMenu(canvas):
    global game_state
    global board
    drawToEntireScreen(canvas, background)  
    drawToEntireScreen(canvas, boardImage)  
    
    # game end state - draw additional text
    if game_state == "end":
        global game_over_message
        global endscreenX
        global endscreenO
        global endscreenTie
        if game_over_message == "O":
            drawToEntireScreen(canvas, endscreenO)
        elif game_over_message == "X":
            drawToEntireScreen(canvas, endscreenX)
        else:
            drawToEntireScreen(canvas, endscreenTie)
        
        # if there's a winner, draw the line connecting the 3 matching slots
        global winner
        if winner:
            global gameOverStateLine
            canvas.draw_line(gameOverStateLine[0], gameOverStateLine[1], 20, "#00bb7890")
    
    # display X and O on the board
    doubleGridSize = gridSize * 2
    topLeftPosition = (150 - doubleGridSize, 150 - doubleGridSize)
    for row in range(3):
        for column in range(3):
            cellDisplay = board[row][column]
            cellPosition = (
                topLeftPosition[0] + (row * doubleGridSize),
                topLeftPosition[1] + (column * doubleGridSize)
            )
            iconDimensions = (playerXImg.get_width(), playerXImg.get_height())
            iconCenter = (playerXImg.get_width() / 2.0, playerXImg.get_height() / 2.0)
            if cellDisplay == "X":
                canvas.draw_image(playerXImg, iconCenter, iconDimensions, cellPosition, (iconSize, iconSize))
            elif cellDisplay == "O":
                canvas.draw_image(playerOImg, iconCenter, iconDimensions, cellPosition, (iconSize, iconSize))
            
    # when a bot is picking a slot (just a delay)
    if game_state == "bot picking":
        global bot_timer
        bot_timer -= 1
        if bot_timer <= 0:
            # when the timer hits 0, the bot picks a slot
            global player
            global bot_x_difficulty
            global bot_o_difficulty
            botPickSlot()
                
            # go to next turn, check for winner, etc.
            continueGame()
            
    # draw the back button
    drawBackArrow(canvas)
            
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Python Tic Tac Toe", 300, 300)
frame.set_draw_handler(mainMenu)
frame.add_button("Reset", resetButtonPressed)
frame.set_mouseclick_handler(mouse_handler)
goToMenu("Main Menu")

# Start the frame animation
frame.start()

# Game variables
game_state = 'continue'
player_x = 'player'
player_o = 'bot'
hardCPUDifficulty = False
player = 'X'
bot_timer = 0
game_over_message = ''
winner = False
board = [
            ['','',''],
            ['','',''],
            ['','','']
        ]

# reset game variables when game starts
def startGame():
    global board
    global player
    global game_state
    board = [
        ['','',''],
        ['','',''],
        ['','','']
    ]
    player = "X"
    game_state = "continue"
    
    # if X is a bot, make it choose a slot
    if player_x == "bot":
        global bot_timer
        bot_timer = 30
        game_state = "bot picking"
 
# game over
def gameOver(message):
    global game_state
    global game_over_message
    game_state = "end"
    game_over_message = message
    print("Game over!")
    print(message)
    
def continueGame():
    global board
    global player
    global game_state
    global winner
    
    # check the board for winners
    if checkWinnerForBoard(board):
        winner = True
        gameOver(player)
        return
    
    # switch turns
    if player == "X":
        player = "O"
    else:
        player = "X"
        
    # check if all slots are filled
    if checkAllSlotsFull(board):
        winner = False
        gameOver("Tie")
        return
        
    # if the next player is a bot, let it pick a slot
    if player == "X" and player_x == "bot":
        game_state = "bot picking"
    if player == "O" and player_o == "bot":
        game_state = "bot picking"
    if game_state == "bot picking":
        global bot_timer
        bot_timer = 30

# when one of the slots have been picked by the player
def gridClicked(row, column):
    global player
    global board
    global game_state
    if board[row][column] != "":
        return # this slot has been picked already
    
    if game_state != "continue":
        return # game cannot progress yet
    
    # fill in the slot with the player (X or O)
    board[row][column] = player
    
    # go to next turn, check for winner, etc.
    continueGame()
  
# checks if the entire board is full
def checkAllSlotsFull(board):
    for row in range(3):
        for column in range(3):
            cell = board[row][column]
            if cell == "":
                return False
    return True

# checks if there's a winner (3 in a row) on a given board
def checkWinnerForBoard(board):
    
    # checks 3 slots and see if they match
    def checkMatching(slot1, slot2, slot3):
        # none of the slots should be blank
        if board[slot1[0]][slot1[1]] == "":
            return False
        if board[slot2[0]][slot2[1]] == "":
            return False
        if board[slot3[0]][slot3[1]] == "":
            return False
        
        # check if the 3 slots are the same value
        if board[slot1[0]][slot1[1]] == board[slot2[0]][slot2[1]] == board[slot3[0]][slot3[1]]:
            
            # calculate the position of the lines to draw in the game over state
            global gameOverStateLine
            global gridSize
            doubleGridSize = gridSize * 2
            topLeftPosition = (150 - doubleGridSize, 150 - doubleGridSize)
            pointA = (
                topLeftPosition[0] + (slot1[0] * doubleGridSize),
                topLeftPosition[1] + (slot1[1] * doubleGridSize)
            )
            pointB = (
                topLeftPosition[0] + (slot3[0] * doubleGridSize),
                topLeftPosition[1] + (slot3[1] * doubleGridSize)
            )
            gameOverStateLine = (
                pointA,
                pointB
            )
            return True
        else:
            return False
    
    # check for rows
    for column in range(3):
        if checkMatching((0,column),(1,column),(2,column)):
            return True
    
    # check for columns
    for row in range(3):
        if checkMatching((row,0),(row,1),(row,2)):
            return True
    
    # check for diagonals
    if checkMatching((0,0),(1,1),(2,2)):
        return True
    if checkMatching((0,2),(1,1),(2,0)):
        return True
    
# stores the position of the line to draw in the game over state
gameOverStateLine = ()
        
# algorithm for when a bot picks a slot
def botPickSlot():
    global player
    global board
    global game_state
    game_state = "continue"
    opponent = "X"
    if player == "X":
        opponent = "O"
    
    # function for randomly picking an available slot
    def randomPick():
        while True:
            selectRow = random.randint(0,2)
            selectColumn = random.randint(0,2)
            if board[selectRow][selectColumn] == "":
                board[selectRow][selectColumn] = player
                break
                
    # function for finding an optimal slot
    def optimalPick():
        
        # first find a slot that allows the bot to win
        for row in range(3):
            for column in range(3):
                if board[row][column] != "":
                    continue
                board[row][column] = player
                if checkWinnerForBoard(board):
                    board[row][column] = player
                    return
                else:
                    board[row][column] = ""
        
        # next find a slot that prevents the player from winning
        for row in range(3):
            for column in range(3):
                if board[row][column] != "":
                    continue
                board[row][column] = opponent
                if checkWinnerForBoard(board):
                    board[row][column] = player
                    return
                else:
                    board[row][column] = ""
                
        # nothing found, pick a random slot
        randomPick()
                
    # depending on difficulty, bot will decide to pick the optimal slot or a random slot
    if hardCPUDifficulty:
        optimalPick()
    else:
        randomPick()
    
