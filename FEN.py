class FEN():
    def __init__(self):
        self.pieces = ['bK','bB', 'bN', 'bR', 'bQ', 'bp',
                       'wK','wB', 'wN', 'wR', 'wQ', 'wp']
        self.FENpieces = {piece:piece[1] for 
                          piece in self.pieces}
        
        for piece in self.FENpieces:
            if piece[0] == 'w':
                self.FENpieces[piece] = self.FENpieces[piece].upper()
            if piece[0] == 'b':
                self.FENpieces[piece] = self.FENpieces[piece].lower()
                
    def positionTOFEN(self, board):
        FENNotation = ""
        for i in range(8):
            rankNotation = ""
            empty = 0
            for j in range(8):
                if(board[i][j]=='__'):
                    empty+=1
                else:
                    if(empty!=0):
                        rankNotation+=f'{empty}'
                        empty=0
                    rankNotation+=self.FENpieces[board[i][j]]
            if empty>0:
                rankNotation+=f'{empty}'
            if i < 7:
                rankNotation+='/'
            FENNotation+=rankNotation
        return FENNotation
