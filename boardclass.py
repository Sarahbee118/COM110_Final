from graphics import *
class Board:

    def __init__(self,win,size): #player variables

        self.size = size #whether big or small
        self.win = win

        if self.size == "small": #if the board is the small
            self.boardCoords = [Point(40,293),Point(111,293),Point(182,293),Point(253,293),Point(324,293),Point(395,293),Point(466,293),Point(537,293),Point(608,293),Point(679,293),Point(679,340),
                                Point(679,393),Point(608,393),Point(537,393),Point(466,393),Point(395,393),Point(324,393),Point(253,393),Point(182,393),Point(111,393),Point(40,393),Point(40,440),
                                Point(40,497),Point(111,497),Point(182,497),Point(253,497),Point(324,497),Point(395,497),Point(466,497),Point(537,497),Point(608,497),Point(679,497)]
            #the locations of all the spaces on the board
            self.ladderSpaces = [5,20] #what spaces have ladders
            self.snakeSpaces = [19,31] #what spaces have snakes
            self.snakes = {31:6, 19:1} #dictionaries tying the location of the one end of the snake/ladder to the other
            self.ladders = {5:26,20:23}

            
        if self.size == "large": #if the board is large
            self.boardCoords = [Point(40,90),Point(111,90),Point(182,90),Point(253,90),Point(324,90),Point(395,90),Point(466,90),Point(537,90),Point(608,90),Point(679,90),Point(679,140),
                                Point(679,190),Point(608,190),Point(537,190),Point(466,190),Point(395,190),Point(324,190),Point(253,190),Point(182,190),Point(111,190),Point(40,190),Point(40,240),
                                Point(40,293),Point(111,293),Point(182,293),Point(253,293),Point(324,293),Point(395,293),Point(466,293),Point(537,293),Point(608,293),Point(679,293),Point(679,340),
                                Point(679,393),Point(608,393),Point(537,393),Point(466,393),Point(395,393),Point(324,393),Point(253,393),Point(182,393),Point(111,393),Point(40,393),Point(40,440),
                                Point(40,497),Point(111,497),Point(182,497),Point(253,497),Point(324,497),Point(395,497),Point(466,497),Point(537,497),Point(608,497),Point(679,497),Point(679,540),
                                Point(679,597),Point(608,597),Point(537,597),Point(466,597),Point(395,597),Point(324,597),Point(253,597),Point(182,597),Point(111,597),Point(40,597)]
            self.ladderSpaces = [5,14, 20,46,53] #what spaces have ladders
            self.snakeSpaces = [32,42,48,51,63] #snakes
            self.snakes = {32:11, 42:22, 48:15, 51:30,63:47} #tying snakes and ladders to the other end
            self.ladders = {5:16,20:58,14:36,46:63,53:57}
                                                                 
                                 

        
    def boardImage(self): #fucntion to return the correct board image
        self.boardimage = Image(Point(360,360),"images/"+(str(self.size)+".png"))

        return self.boardimage


    def snake(self,win,current,player): #function to tell what to do if the player lands on a snake
        
        
        player[current].position = self.snakes[player[current].position]
        return player
    
    def ladder(self,win,current,player): #function to tell what to do if the player lands on a ladder
        
        
        player[current].position = self.ladders[player[current].position]
        return player
        



##def main():
##    win = GraphWin("BlackJack",720,720) #draw window
##    win.setCoords(0,0,720,720) #set window size
##    image = Image(Point(360,360),"large.png")
##    image.draw(win)
##    e = [Point(40,90),Point(111,90),Point(182,90),Point(253,90),Point(324,90),Point(395,90),Point(466,90),Point(537,90),Point(608,90),Point(679,90),Point(679,140),
##                                Point(679,190),Point(608,190),Point(537,190),Point(466,190),Point(395,190),Point(324,190),Point(253,190),Point(182,190),Point(111,190),Point(40,190),Point(40,240),
##                                Point(40,293),Point(111,293),Point(182,293),Point(253,293),Point(324,293),Point(395,293),Point(466,293),Point(537,293),Point(608,293),Point(679,293),Point(679,340),
##                                Point(679,393),Point(608,393),Point(537,393),Point(466,393),Point(395,393),Point(324,393),Point(253,393),Point(182,393),Point(111,393),Point(40,393),Point(40,440),
##                                Point(40,497),Point(111,497),Point(182,497),Point(253,497),Point(324,497),Point(395,497),Point(466,497),Point(537,497),Point(608,497),Point(679,497),Point(679,540),
##                                Point(679,597),Point(608,597),Point(537,597),Point(466,597),Point(395,597),Point(324,597),Point(253,597),Point(182,597),Point(111,597),Point(40,597)]
##    for i in range(len(e)):
##        e[i].draw(win)
##
##main()
