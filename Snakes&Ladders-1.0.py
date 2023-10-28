# Chutes and Ladders
from graphics import * #importing graphics
from buttonclass import * #importing the button, however this has been slightly modified to remove the image of the button, the button images are used instead
from boardclass import * #board class imported
from playerclass import * #importing board class
from time import * #import time
from random import * #import time
from die import * #import die
from sys import * #import sys


def titlescreen(win): #titlescreen function de
    
    backgroundTitle = Image(Point(360,360),"images/background.png")
    backgroundTitle.draw(win)
    logo = Image(Point(360,500),"images/logo.png")
    logo.draw(win)
    #The images on the title screen
                 
    startButton = Button(win,Point(360,200),200,100,"START!")
    instructionButton=Button(win,Point(360,120),200,30,"")
    backButton = Button(win,Point(55,690),100,50,"")
    backImage = Image(Point(55,690),"images/backButton.png")
    instructions = Image(Point(360,360),"images/instructions.png")
    instructionImage = Image(Point(360,120),"images/instructionButton.png").draw(win)
    startButtonimage = Image(Point(360,200),"images/startButtonpng.png")
    
    startButtonimage.draw(win)
    startButton.activate()
    instructionButton.activate()
    backButton.activate()
    #buttons needed to use the start menu, the start button, and instructions, back button for instructions are also included.
    
    pt = win.getMouse() #getting click
    while not startButton.clicked(pt): #while loop waiting start to click
        if instructionButton.clicked(pt): #check if instruction button 
            instructions.draw(win)
            backImage.draw(win)
            while not backButton.clicked(pt): #wait until user wants to go back to title screen
                pt = win.getMouse()
            instructions.undraw()
            backImage.undraw()
                
                                
        pt = win.getMouse() #get mouse click repeatedly
        
    startButton.rect.undraw()
    startButton.label.undraw()
    logo.undraw()
    startButtonimage.undraw()
    backgroundTitle.undraw()
    #when start menu is over it undraws everything


def manVSmachine(win):
    backgroundMenus = Image(Point(360,360),"images/backgroundmenus.png").draw(win)
    players = Image(Point(360,360),"images/players.png").draw(win)
    
    areCPU = ["null",False,False,False,False] #to keep things simple, as there are 4 players instead of having most lists related to players be 1-4 and not 0-3
    cpu1 = Button(win,Point(180+37.5+5,180+100),75,75,"CPU")
    human1 = Button(win,Point(180-37.5-5,180+100),75,75,"Player")
    #each of these is a button to pick between whetehr a player is a computer or a human
    #these are all math because I started adjusting it with math and it eventually got out of hand. It works however, and makes for easy adjusting
    cpu2 = Button(win,Point(180+37.5+5,360+180-100),75,75,"CPU")
    human2 = Button(win,Point(180-37.5-5,360+180-100),75,75,"Player")
    cpu3 = Button(win,Point(360+180+37.5+5,180+100),75,75,"CPU")
    human3 = Button(win,Point(360+180-37.5-5,180+100),75,75,"Player")
    cpu4 = Button(win,Point(360+180+37.5+5,360+180-100),75,75,"CPU")
    human4 = Button(win,Point(360+180-37.5-5,360+180-100),75,75,"Player")
    nextButton = Button(win,Point(660,40),70,40,"Next")
    cpu1Button =Image(Point(180+37.5+5,180+100),"images/cpuselect.png")
    human1Button =Image(Point(180-37.5-5,180+100),"images/humanselect.png")
    cpu2Button =Image(Point(180+37.5+5,360+180-100),"images/cpuselect.png")
    human2Button =Image(Point(180-37.5-5,360+180-100),"images/humanselect.png")
    cpu3Button =Image(Point(360+180+37.5+5,180+100),"images/cpuselect.png")
    human3Button =Image(Point(360+180-37.5-5,180+100),"images/humanselect.png")
    cpu4Button =Image(Point(360+180+37.5+5,360+180-100),"images/cpuselect.png")
    human4Button =Image(Point(360+180-37.5-5,360+180-100),"images/humanselect.png")
    nextImage = Image(Point(660,40),"images/next.png") #button to move on to next menu
    
    #drawing an activating all of thebuttons
    nextImage.draw(win)
    nextButton.activate()
    cpu1.activate()
    human1.activate()
    cpu2.activate()
    human2.activate()
    cpu3.activate()
    human3.activate()
    cpu4.activate()
    human4.activate()
    cpu1Button.draw(win)
    human1Button.draw(win)
    cpu2Button.draw(win)
    human2Button.draw(win)
    cpu3Button.draw(win)
    human3Button.draw(win)
    cpu4Button.draw(win)
    human4Button.draw(win)
    
    #these are the red boarders around the options 
    rect1 = Image(Point(180-37.5-5,180+100),"images/selectaround.png").draw(win)
    rect4 = Image(Point(360+180-37.5-5,360+180-100),"images/selectaround.png").draw(win)
    rect2 = Image(Point(180-37.5-5,360+180-100),"images/selectaround.png").draw(win)
    rect3 = Image(Point(360+180-37.5-5,180+100),"images/selectaround.png").draw(win)
    pt = win.getMouse()
    
    while not nextButton.clicked(pt): # waiting for the user to hit next

        #checking if the cpu button is clicked 
        if cpu1.clicked(pt):
            rect1.undraw()
            rect1 = Image(Point(180+37.5+5,180+100),"images/selectaround.png").draw(win)
            areCPU[1] = True

        #checking if human button is clicked
        #the rest do the same but for the other players
        if human1.clicked(pt):
            rect1.undraw()
            rect1 = Image(Point(180-37.5-5,180+100),"images/selectaround.png").draw(win)
            areCPU[1] = False

        if cpu2.clicked(pt):
            rect2.undraw()
            rect2 = Image(Point(180+37.5+5,360+180-100),"images/selectaround.png").draw(win)
            areCPU[2] = True

        if human2.clicked(pt):
            rect2.undraw()
            rect2 = Image(Point(180-37.5-5,360+180-100),"images/selectaround.png").draw(win)
            areCPU[2] = False

        if cpu3.clicked(pt):
            rect3.undraw()
            rect3 = Image(Point(360+180+37.5+5,180+100),"images/selectaround.png").draw(win)
            areCPU[3] = True

        if human3.clicked(pt):
            rect3.undraw()
            rect3 = Image(Point(360+180-37.5-5,180+100),"images/selectaround.png").draw(win)
            areCPU[3] = False

        if cpu4.clicked(pt):
            rect4.undraw()
            rect4 = Image(Point(360+180+37.5+5,360+180-100),"images/selectaround.png").draw(win)
            areCPU[4] = True

        if human4.clicked(pt):
            rect4.undraw()
            rect4 = Image(Point(360+180-37.5-5,360+180-100),"images/selectaround.png").draw(win)
            areCPU[4] = False
            
        
        pt = win.getMouse()  #get the mouse click for the while loop
    return areCPU #informs the main game if which players are human and which are CPUs
    
                  
        


def characterselect(win): #character select function
    Image(Point(360,360 ),"images/backgroundmenus.png").draw(win) #the background image, a nice shade of blue
    pt = Point(0,0) #resetting point to 0,0 just to keep it away from the buttons, just to make sure the last click won't hit a button
    colorlist = ["null",] #the first instance, 
    charSelect = Image(Point(360,610),"images/pieceselect.png") #Image labeling the screen
    charSelect.draw(win)
    redButton = Button(win,Point(260,460),100,100,"Red") #The buttons to pick each color
    orangeButton = Button(win,Point(360,460),100,100,"Orange")
    yellowButton = Button(win,Point(460,460),100,100,"Yellow")
    greenButton = Button(win,Point(260,260),100,100,"Green")
    blueButton = Button(win,Point(360,260),100,100,"Blue")
    purpleButton = Button(win,Point(460,260),100,100,"Purple")
    #See the read me on more info on Pink,Brown, and White
    pinkButton = Button(win,Point(260,360),100,100,"Pink")
    brownButton = Button(win,Point(360,360),100,100,"Brown")
    whiteButton = Button(win,Point(460,360),100,100,"White")
    #The images that make up the color select 
    redB = Image(Point(260,460),"images/redselect.png")
    redB.draw(win)
    orangeB = Image(Point(360,460),"images/orangeselect.png")
    orangeB.draw(win)
    yellowB = Image(Point(460,460),"images/yellowselect.png")
    yellowB.draw(win)
    greenB = Image(Point(260,260),"images/greenselect.png")
    greenB.draw(win)
    blueB = Image(Point(360,260),"images/blueselect.png")
    blueB.draw(win)
    purpleB = Image(Point(460,260),"images/purpleselect.png")
    purpleB.draw(win)
    brownB = Image(Point(360,360),"images/brownselect.png")
    brownB.draw(win)
    whiteB = Image(Point(460,360),"images/whiteselect.png")
    whiteB.draw(win)
    pinkB = Image(Point(260,360),"images/pinkselect.png")
    pinkB.draw(win)
    #activating all of the buttons
    redButton.activate()
    purpleButton.activate()
    orangeButton.activate()
    yellowButton.activate()
    greenButton.activate()
    blueButton.activate()
    whiteButton.activate()
    pinkButton.activate()
    brownButton.activate()

    #defining the player select
    playerSelect = 1
    

    while playerSelect < 5: #until all 4 players have colors
        playerTurn = Image(Point(360,40),("images/"+str(playerSelect)+"turn.png")).draw(win)  #Telling user which player color is picked 
        pt = win.getMouse()
        #getting the cli  


       #each of these is a button being clicked
        if redButton.clicked(pt):
            colorlist.append("red") #what color it should be
            playerSelect = playerSelect + 1 #bump up the player list
            Image(Point(260,460),"images/redselected.png").draw(win) #change image to make it clear you cant select it any more
            redButton.deactivate() #deactivate the button
            redB.undraw() #remove it from existence
            #all the following are the same for different colors
        if orangeButton.clicked(pt):
            colorlist.append("orange")
            playerSelect = playerSelect + 1
            Image(Point(360,460),"images/orangeselected.png").draw(win)
            orangeB.undraw()
            orangeButton.deactivate()
        if yellowButton.clicked(pt):
            colorlist.append("yellow")
            Image(Point(460,460),"images/yellowselected.png").draw(win)
            yellowB.undraw()
            playerSelect = playerSelect + 1
            yellowButton.deactivate()
        if greenButton.clicked(pt):
            colorlist.append("green")
            Image(Point(260,260),"images/greenselected.png").draw(win)
            playerSelect = playerSelect + 1
            greenB.undraw()
            greenButton.deactivate()
        if blueButton.clicked(pt):
            colorlist.append("blue")
            Image(Point(360,260),"images/blueselected.png").draw(win)
            blueB.undraw()
            playerSelect = playerSelect + 1
            blueButton.deactivate()
        if purpleButton.clicked(pt):
            colorlist.append("purple")
            Image(Point(460,260),"images/purpleselected.png").draw(win)
            purpleB.undraw()
            playerSelect = playerSelect + 1
            purpleButton.deactivate()
        if brownButton.clicked(pt):
            colorlist.append("brown")
            Image(Point(360,360),"images/brownselected.png").draw(win)
            playerSelect = playerSelect + 1
            brownB.undraw()
            brownButton.deactivate()
        if pinkButton.clicked(pt):
            colorlist.append("pink")
            Image(Point(260,360),"images/pinkselected.png").draw(win)
            pinkB.undraw()
            playerSelect = playerSelect + 1
            pinkButton.deactivate()
        if whiteButton.clicked(pt):
            colorlist.append("white")
            whiteB.undraw()
            Image(Point(460,360),"images/whiteselected.png").draw(win)
            
            playerSelect = playerSelect + 1
            whiteButton.deactivate()
        playerTurn.undraw() #undraw current player turn
    
    return colorlist #give the color list to the main game
    
def boardSelect(win): #selecting which size board to pick
    Image(Point(360,360),"images/backgroundmenus.png").draw(win) #draw the background 
    pt = Point(0,0) #reset pt to make sure it wont accidently be carried over 
    large = Button(win,Point(180,360),200,200,"large") #the button for the large board
    small = Button(win,Point(540,360),200,200,"small") #the button for the small board
    small.activate() #activate the buttons
    large.activate()
    options = [Image(Point(540,360),"images/smallselect.png").draw(win),Image(Point(180,360),"images/largeselect.png").draw(win)] #Discovering you can draw images like this, drawing the two images for sizes
    while not large.clicked(pt) and not small.clicked(pt): #wait for one to be clicked
        pt = win.getMouse() #get the click
        if small.clicked(pt): #small is clicked
            return "small" #returns the small string for main game 
        if large.clicked(pt):
            return "large" #returns the large string for the main game
    

    


def mainGame(win,playerColors,CPU,size): #the main game, not main but the main game
        gameBackground = Image(Point(360,360),"images/background.png").draw(win) #draws the background
        gameBoard = Board(win,size) #takes the inputs to draw the correct sized board, and set all variables correctly
        exitButton = Button(win, Point(650,40), 60, 30, "Exit") #exit buton
        rollButton = Button(win, Point(50,40), 60, 30, "Roll Dice") #dice roll button
        exitImage = Image(Point(670,40),"images/exitButton.png").draw(win) #the images associated with those buttons
        rollImage = Image(Point(50,40),"images/rollButton.png").draw(win) 
        exitButton.activate() #activate the buttons 
        rollButton.activate()
        snake = gameBoard.snakeSpaces #which snakes the board size has
        ladder = gameBoard.ladderSpaces #which ladders the board size has
        locationStore = ["null","e","e","e","e"] #setting up the laction store list
        player = ["null",Player(win,1,playerColors[1],0,12,18,CPU[1]),Player(win,1,playerColors[2],0,-12,-5,CPU[2]),Player(win,1,playerColors[3],0,-12,18,CPU[3]),Player(win,1,playerColors[4],0,12,-5,CPU[4])]
        #The players themselves. Defined more in player class
        current = 1 #player 1 begins
        rolled = False #making roll false
    
        
        gameBoard.boardImage().draw(win) #actually draws the board
        pt = Point(0,0) #point reset
        
        while not exitButton.clicked(pt): #untile someone exits
            while player[1].position <= len(gameBoard.boardCoords) and player[2].position < len(gameBoard.boardCoords) and player[3].position < len(gameBoard.boardCoords) and player[4].position < len(gameBoard.boardCoords):
            #Checking if a player has made it to the end to know the end the loop
            
                while rolled == False: #wait until someone clicks roll
                    turn = Image(Point(360,40),("images/"+str(current)+"turn.png")).draw(win) #drawing who's turn it is
                    
                                          
                                 
                    if player[current].CPU == False: #if the player isn't a human
                        if exitButton.clicked(pt): #check if exit button was the one that was clicked
                            win.close() #close windows
                            sys.exit() #stops program
                            
                        if rollButton.clicked(pt): #if the roll button is clicked
                           #  print(locationStore[current]) Debugger line, used to test 
                            rolled = True #the player has now rolled 
                            if type(locationStore[current]) is not str: #any time after the first roll
                                locationStore[current].undraw() #undraws the piece from the last time this player has a turn
                            die1 = die(win, Point(360,670),50) #The die
                            if die1.getValue() + player[current].position > len(gameBoard.boardCoords): #if the player rolls past the end, they need to get it exact
                                locationStore[current].draw(win) #draw the piece
                                
                            else: #any other scenario
                                for i in range (die1.getValue()): #for how whater number is on the die
                                    currentpiece = Image(Point(gameBoard.boardCoords[player[current].position].getX()+player[current].xOffset,gameBoard.boardCoords[player[current].position].getY()+player[current].yOffset),"images/"+player[current].color+".png")
                                    #the current piece is moving
                                    currentpiece.draw(win)
                                    player[current].updatePos() #updates the position
                                    sleep(.5) #stop for a second
                                    currentpiece.undraw() #undraw the piece
                                
                               
                                locationStore[current] = currentpiece #store where the piece is 
                                locationStore[current].draw(win) #draw this piece
                            if player[current].position in snake: #check if it is on the top of a snake
                                sleep(.5) #wait for .5
                                locationStore[current].undraw() #undraw the piece
                                player = gameBoard.snake(win,current,player) #the player is updated based on which snake, see board class for more
                                locationStore[current] = Image(Point(gameBoard.boardCoords[player[current].position].getX()+player[current].xOffset,gameBoard.boardCoords[player[current].position].getY()+player[current].yOffset),"images/"+player[current].color+".png")
                                #storing new image/location
                                locationStore[current].draw(win) #drawing this
                                player[current].updatePos() #update position
                                sleep(.5) #wait for .5 seconds
                                
                            if player[current].position in ladder: #same for snakes but it's the ladders
                                sleep(.5)
                                locationStore[current].undraw()
                                player = gameBoard.ladder(win,current,player)
                                locationStore[current] = Image(Point(gameBoard.boardCoords[player[current].position].getX()+player[current].xOffset,gameBoard.boardCoords[player[current].position].getY()+player[current].yOffset),"images/"+player[current].color+".png")
                                locationStore[current].draw(win)
                                player[current].updatePos()
                                sleep(.5)

                                
                            if die1.getValue() + player[current].position == len(gameBoard.boardCoords): #checks if the player has won
                                sleep(.5) #wait .5 
                                gameBackground.undraw() #undraws some objects
                                gameBoard.boardimage.undraw()
                                exitImage.undraw()
                                return current,player #back to main, with needed variables
                            if player[1].position < len(gameBoard.boardCoords) and player[2].position < len(gameBoard.boardCoords) and player[3].position < len(gameBoard.boardCoords) and player[4].position < len(gameBoard.boardCoords):
                            #other scenarios
                                if current < 4: #if turn 1-3
                                    current = current + 1 #next player turn
                                else:
                                    current = 1 #if turn 4, back to 1
                            pt = Point(0,0)
                                
                        if rolled == False: #if the user didn't click
                            pt = win.getMouse() #get click again 
                        turn.undraw() #undraw turn coutner
                    
                    if player[current].CPU == True: #if the player is a computer
                        
                        rolled = True #rolled is automatically true because the program can't click
                        #all else is essentailly the same from when a human rolls
                            
                        die1 = die(win, Point(360,670),50) #roll die
                        if die1.getValue() + player[current].position > len(gameBoard.boardCoords): 
                                

                                locationStore[current].undraw()
                                locationStore[current].draw(win)
                                
                                
                                
                                
                        
                        else:
                            
                            if type(locationStore[current]) is not str:
                                locationStore[current].undraw()
                            
                            for i in range (die1.getValue()):
                                
                                currentpiece = Image(Point(gameBoard.boardCoords[player[current].position].getX()+player[current].xOffset,gameBoard.boardCoords[player[current].position].getY()+player[current].yOffset),"images/"+player[current].color+".png")
                                currentpiece.draw(win)
                                player[current].updatePos()
                                sleep(.3)
                                currentpiece.undraw()
                        
                          #  print("Current is",current)
                            locationStore[current] = currentpiece
                            locationStore[current].draw(win)
                            
                            if player[current].position in snake:
                                sleep(.5)
                                locationStore[current].undraw()
                                player = gameBoard.snake(win,current,player)
                                locationStore[current] = Image(Point(gameBoard.boardCoords[player[current].position].getX()+player[current].xOffset,gameBoard.boardCoords[player[current].position].getY()+player[current].yOffset),"images/"+player[current].color+".png")
                                locationStore[current].draw(win)
                                player[current].updatePos()
                                sleep(.5)
                                
                            if player[current].position in ladder:
                                sleep(.5)
                                locationStore[current].undraw()
                                player = gameBoard.ladder(win,current,player)
                                locationStore[current] = Image(Point(gameBoard.boardCoords[player[current].position].getX()+player[current].xOffset,gameBoard.boardCoords[player[current].position].getY()+player[current].yOffset),"images/"+player[current].color+".png")
                                locationStore[current].draw(win)
                                player[current].updatePos()
                                sleep(.5)
                           # print(locationStore[current])
                            
                        if  player[current].position == len(gameBoard.boardCoords):
                                sleep(.5)
                                gameBackground.undraw()
                                gameBoard.boardimage.undraw()
                                exitImage.undraw()
                                rollImage.undraw()
                                
                                Exit = False
                                return current,player,Exit
                            
                        if player[1].position < len(gameBoard.boardCoords) and player[2].position < len(gameBoard.boardCoords) and player[3].position < len(gameBoard.boardCoords) and player[4].position < len(gameBoard.boardCoords):

                            if current < 4:
                                current = current + 1
                            else:
                                current = 1
                        pt = Point(0,0)
                            
                
                    turn.undraw()      
                rolled = False #changes roll back to false for next turn
               
                
                

           
            pt = win.getMouse() #geting the mouse click


def winscreen(win,winner,players,Exit): #Win Scree
    playAgain = False #Play again is defined and set to fall
    
    winnerColor = Rectangle(Point(720,0),Point(0,720)) #makes a large rectangle of the color of the winner
    winnerColor.setFill(players[winner].color) 
    winnerColor.draw(win)
    
    winner = Image(Point(360,360),"images/p"+str(winner)+"Wins.png").draw(win) #draws the image for the win screen
    #The rectangle shows through the blank pixels in the image to color the lettering
    #This is similar to how the MacBook I'm working on right now does the apple light, with there being a cut out in the casing and the screens light shines through
    playAgain = Button(win,Point(100,120),100,50,"Play Again") #play again button
    exitButton = Button(win,Point(640,120),100,50,"Exit") #exit button
    exitImage = Image(Point(640,120),"images/exitButton2.png").draw(win) #image of button
    playAgainImage = Image(Point(100,120),"images/playAgainButton.png").draw(win) #image for play again
    playAgain.activate() #activates the buttons 
    exitButton.activate()
    pt = win.getMouse() #our old friend mouse click
    
    while not exitButton.clicked(pt): #wait until exit is clicked
        if playAgain.clicked(pt): #see if the player clicked play again 
            Exit = False #returns exit with false so while loop will continue
            winnerColor.undraw() #undraws all in fucntion
            winner.undraw()
            exitImage.undraw()
            playAgainImage.undraw()
            return Exit #exit function
        pt = win.getMouse() #mouse click mouse click


    Exit = True #exit is now tru
    winnerColor.undraw() #undraws all in fucntion
    winner.undraw()
    exitImage.undraw()
    playAgainImage.undraw()
    
    return Exit #exit the program

    
        




def main(): #the main function
    Exit = False #start
   # currentpiece = "null"
    win = GraphWin("Snakes & Ladders",720,720) #draw window
    win.setCoords(0,0,720,720) #set window size
    win.setBackground(color_rgb(0,27,63)) #set the background color
    titlescreen(win) #starts the title screen
    CPUs = manVSmachine(win) #starts whether computer or human screen function
    size = boardSelect(win) #starts board size screen function
    playerColors = characterselect(win) #start character select screen function
    while Exit == False: #while loop to run game is exited
        winner,players,Exit = mainGame(win,playerColors,CPUs,size) #the main game function
    
        Exit = winscreen(win,winner,players,Exit) #the win screen function
    win.close()

    
if __name__ == "__main__":
    main() #main
