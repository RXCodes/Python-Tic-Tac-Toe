import simplegui

def resetButtonPressed():
    goToMenu("Main Menu")

# Changes the menu
def goToMenu(name):
    global frame
    if name == "Main Menu":
        global mainMenu
        frame.set_draw_handler(mainMenu)
    if name == "Board Menu":
        global boardMenu
        frame.set_draw_handler(boardMenu)

# Check if point is inside rectangle
def rectangleCheck(position, rectX, rectY, rectX2, rectY2):
    if position[0] >= rectX and position[0] <= rectX2:
        if position[1] >= rectY and position[1] <= rectY2:
            return True
    return False
        
# Handle mouse clicks
def mouse_handler(position):
    print(position)
    
    # when click on "Play Game" button
    if rectangleCheck(position, 40, 230, 230, 260):
        goToMenu("Board Menu")
    
# Handler to draw menus
def mainMenu(canvas):
    canvas.draw_text("Python Tic Tac Toe", [50,50], 26, "White")
    canvas.draw_text("Play Game", [50,250], 18, "Yellow")
    
def boardMenu(canvas):
    canvas.draw_text("Board", [118,25], 26, "White")
    gridSize = 30
    extendSize = gridSize * 2
    
    # horizontal lines
    canvas.draw_line((150 - gridSize - extendSize, 150 - gridSize), (150 + gridSize + extendSize, 150 - gridSize), 3, "Gray")
    canvas.draw_line((150 - gridSize - extendSize, 150 + gridSize), (150 + gridSize + extendSize, 150 + gridSize), 3, "Gray")
    
    # vertical lines
    canvas.draw_line((150 - gridSize, 150 - gridSize - extendSize), (150 - gridSize, 150 + gridSize + extendSize), 3, "Gray")
    canvas.draw_line((150 + gridSize, 150 - gridSize - extendSize), (150 + gridSize, 150 + gridSize + extendSize), 3, "Gray")
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Python Tic Tac Toe", 300, 300)
frame.set_draw_handler(mainMenu)
frame.add_button("Reset", resetButtonPressed)
frame.set_mouseclick_handler(mouse_handler)
goToMenu("Main Menu")

# Start the frame animation
frame.start()
