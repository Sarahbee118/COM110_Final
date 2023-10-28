This is the final project of the Intro To Computer Sciences Class (COM110) At Connecticut College



Sarah Rigg and Safa Farooqui

Snakes and Ladders

Purpose: The purpose of this project was to create a video game version of the classic game Snakes and Ladders. 

Program Itself: The program is broken down into several functions, as well as serval objects. Once the main function is called it begins by creating the window for the game to be played in. It then goes down through different functions, each being a different menu in getting to the game. The titlescreen function only takes in win, all future functions in main do as well, at its only purpose is to be a title screen. No variables need be returned. The mainVSmachine function is the screen where players pick which players are Human and which computers (hence the name) it returns the variable CPUs which will be used later. boardSelect and characterselect are very similar returning size and playerColors respectively. These are also used later. A while loop is used to contain the main parts of the game. This takes in all three aforementioned variables, and win of course. The main logic of the game all lives in here. It uses the three variables to assign attributes to the objects of board and player. The board just holds all the information about the board. The players are all stored in a list and contain information on where they are, their color, are they controlled by the computer or not. mainGame function itself is what puts all those pieces together. It returns winner, players, and exit. Winners is just the current turn it is. Players is returned for the purpose of pulling the color in winscreen. in winscreen takes in these variables and only returns Exit. Only when it returns Exit as true with the program end and the window close


Testing and Revisions: Testing was done by having a multitude of combination of colors, player types, and boards tested for full games, and even play again. Features were also tested as they were implemented. The most limiting factor for this project was time. We didn't have the time to add music or sound effects like we had originally hoped. Another thing limited by time is originally Pink, Black, and Brown pieces were going to be locked behind requirements (Play on short board 1 time: Pink, Play on Large Board 1 Time: Brown, Play 10 Games in one sitting: White) and have the program write to a text file so that any time the program was ran after that it could look in that text file to unlock those pieces. Essentially we wanted to add saving. Other features we believe would be good to add would be more fluid animation, and the ability to name your piece.


Credits:
Programming: Bee Rigg & Safa Farooqui
Graphics: Bee Rigg
Snake Chan Font: Darrell Flood (https://www.fontspace.com/darrell-flood)
Snakes and Ladders Art: Beau Ma


