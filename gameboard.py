class Gameboard:    
    def __init__(self):
        self.board = {}
        self.powertiles = {}
        self.letterValues = {}

#############################################################################################    
#    All board tiles are stored in two dictionaries - one with powertiles, one with letters #
#    Key: grid coordinates from 1x1 up to 15x15                                             #
#    Entry: letter (if no letter -> None), powertile (options: 2l, 3l, 2w, 3w, None)        #
#############################################################################################
   
    # setup the raw board
    def standardEmptyBoard(self):
        column = 1
        row = 1
        # 15x15 gameboard
        while column < 16:
            while row < 16:
                self.board[column, row] = None
                row += 1
            column += 1
            row = 0

    def standardPowerTiles(self):
        # set double word tiles
        column = 2
        row = 2
        while column < 16:
            while row < 16:
                self.powertiles[column, row] = '2w'
                row +=1
                column +=1

        column = 1
        row = 15
        while column < 16:
            while row > 1:
                self.powertiles[column, row] = '2w'
                row -=1
                column +=1
            column +=1
        
        # set triple word tiles
        self.powertiles[1,1] = '3w'
        self.powertiles[8,1] = '3w'
        self.powertiles[15,1] = '3w'
        self.powertiles[1,8] = '3w'
        self.powertiles[15,8] = '3w'
        self.powertiles[1,15] = '3w'

        # set double letter tiles
        self.powertiles[4,1] = '2l'
        self.powertiles[12,1] = '2l'

        self.powertiles[7,3] = '2l'
        self.powertiles[9,3] = '2l'

        self.powertiles[1,4] = '2l'
        self.powertiles[8,4] = '2l'
        self.powertiles[15,4] = '2l'

        self.powertiles[3,7] = '2l'
        self.powertiles[7,7] = '2l'
        self.powertiles[9,7] = '2l'
        self.powertiles[13,7] = '2l'

        self.powertiles[3,8] = '2l'
        self.powertiles[12,8] = '2l'

        self.powertiles[3,9] = '2l'
        self.powertiles[7,9] = '2l'
        self.powertiles[9,9] = '2l'
        self.powertiles[13,9] = '2l'

        self.powertiles[1,12] = '2l'
        self.powertiles[8,12] = '2l'
        self.powertiles[15,12] = '2l'

        self.powertiles[7,13] = '2l'
        self.powertiles[9,13] = '2l'

        self.powertiles[4,15] = '2l'
        self.powertiles[12,15] = '2l'

        # set triple letter tiles
        self.powertiles[6,2] = '3l'
        self.powertiles[10,2] = '3l'

        self.powertiles[2,6] = '3l'
        self.powertiles[6,6] = '3l'
        self.powertiles[10,6] = '3l'
        self.powertiles[14,6] = '3l'
        
        self.powertiles[2,10] = '3l'
        self.powertiles[6,10] = '3l'
        self.powertiles[10,10] = '3l'
        self.powertiles[14,10] = '3l'
        
        self.powertiles[6,14] = '3l'
        self.powertiles[10,14] = '3l'

    def initialLayout(self):
        row = 1
        column = 1
        while row < 16:
            rowStr = ''
            while column < 16:
                if (row,column) in self.powertiles:
                    rowStr += self.powertiles[row,column] + " "
                else:
                    rowStr += "[] "
                column += 1
            print rowStr
            row += 1
            column = 1

    def letterVals(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter in alphabet:
            self.letterValues[letter] = 1
        self.letterValues['d'] = 2
        self.letterValues['g'] = 2
        
        self.letterValues['b'] = 3
        self.letterValues['c'] = 3
        self.letterValues['m'] = 3
        self.letterValues['p'] = 3

        self.letterValues['f'] = 4
        self.letterValues['h'] = 4
        self.letterValues['v'] = 4
        self.letterValues['w'] = 4
        self.letterValues['y'] = 4

        self.letterValues['k'] = 5
        
        self.letterValues['j'] = 8
        self.letterValues['x'] = 8
        self.letterValues['q'] = 10
        self.letterValues['z'] = 10

#        for letter in alphabet:
#            print letter + " -->" + str(self.letterValues[letter])
