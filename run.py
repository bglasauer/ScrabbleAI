import gameboard
import validWords

#load up the valid word dictionary
words = validWords.validWords()
words.loadWords()

#initialize empty gameboard, power tiles and letter points
board = gameboard.Gameboard()
board.standardEmptyBoard()
board.standardPowerTiles()
board.letters()
board.layout()
