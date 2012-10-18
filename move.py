import gameboard
import validWords


def isValidWord (word, validWords):
    temp = list(word)
    temp.sort()
    key = ''.join(temp)
    if key not in validWords.words.keys():
        return False
    else:
        possEntries = validWords.words[key]
        if word not in possEntries:
            return False
        else:
            return True

def canPlaceThere (word, board, (startx, starty), direction):
    wordLen = len(word)
    i = 0
    if direction == 'right':
        row = starty
        column = startx
        while i < wordLen:
            if board.board[column,row] != None:
                return False
            column += 1
            i+=1
        return True
    if direction == 'down':
        row = starty
        column = startx
        while i < wordLen:
            if board.board[column,row] != None:
                return False
            row += 1
            i+=1
        return True    

def placeOnBoard (word, board, (startx, starty), direction):
    move = list(word)
    movelen = len(move)
    total = 0
    multiplier = 1
    if direction == 'right':
        row = starty
        column = startx
        for letter in move:
            letterScore = board.letterValues[letter]
            board.board[column, row] = letter.upper()
            if (column, row) in board.powertiles.keys():
                if board.powertiles[column,row] == '2l':
                    letterScore = letterScore * 2
                elif board.powertiles[column,row] == '3l':
                    letterScore = letterScore * 3
                elif board.powertiles[column,row] == '2w':
                    multiplier = multiplier * 2
                elif board.powertiles[column,row] == '3w':
                    multiplier = multiplier * 3
            column += 1
            total += letterScore
    if direction == 'down':
        row = starty
        column = startx
        for letter in move:
            letterScore = board.letterValues[letter]
            board.board[column, row] = letter.upper()
            if (column, row) in board.powertiles.keys():
                if board.powertiles[column,row] == '2l':
                    letterScore = letterScore * 2
                elif board.powertiles[column,row] == '3l':
                    letterScore = letterScore * 3
                elif board.powertiles[column,row] == '2w':
                    multiplier = multiplier * 2
                elif board.powertiles[column,row] == '3w':
                    multiplier = multiplier * 3
            row += 1
            total += letterScore

    return total * multiplier

    
            
    
words = validWords.validWords()
words.loadWords()

board = gameboard.Gameboard()
board.standardEmptyBoard()
board.standardPowerTiles()
board.letters()

if not isValidWord ('apelpe', words):
    print 'good!'

if not isValidWord ('fdfdfdf', words):
    print 'good also'

blah = placeOnBoard ('apple', board, (1,1), 'right')
print blah
bing = placeOnBoard('orange', board, (13,1), 'down')
board.layout()
print canPlaceThere ('apple', board, (1,2), 'down')

