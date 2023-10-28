#player class
#Designed by Bee Rigg


class Player: #class name

    def __init__(self,win,name,color,position,xOffset,yOffset,CPU): #player variables

        self.name = name #what name (#) the player is
        self.color = color #the color of the piece
        self.position = position #where along the board
        self.win = win #win
        self.xOffset = xOffset #an x and y offset so the pieces wont overlap
        self.yOffset = yOffset
        self.CPU = CPU #whether or not they're a computer player

    def getPos(): #checking the position

        return self.position

        
    def updatePos(self): #updates position after player moves

        self.position = self.position + 1
    
