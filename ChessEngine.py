class GameState():
    def __init__(self):
        self.board = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                      ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                      ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        
        self.whiteToMove = True
        self.moveLogs = []
        self.moveFunctions = {"p": self.getPawnMoves, "R": self.getRookMoves,
                              "N":self.getKnightMoves, "B": self.getBishopMoves,
                              "K":self.getKingMoves, "Q": self.getQueenMoves}
    
    def makeMove(self, move):
        if move.pieceMoved == '__':
            pass
        else:
            self.board[move.startRow][move.startCol] = '__'
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moveLogs.append(move)
            self.whiteToMove = not self.whiteToMove
    
    def undoMove(self):
        if len(self.moveLogs) != 0:
            move = self.moveLogs.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
    
    def getValidMoves(self):
        return self.getAllPossibleMoves()
    
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r, c, moves)
        return moves
                        
    
    def displayPossibleMoves(self, r, c, moves):
        cells_to_be_highlighted = []
        for move in moves:
            if (r, c) == (move.startRow, move.startCol):
                cells_to_be_highlighted.append((move.endRow, move.endCol))
        return cells_to_be_highlighted
    
    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove:
            if r-1>=0:    
                if self.board[r-1][c] == "__":
                    moves.append(Move((r,c), (r-1, c), self.board))
                    if r == 6 and self.board[r-2][c] == "__":
                        moves.append(Move((r,c), (r-2, c), self.board))
                if c-1>=0:
                    if self.board[r-1][c-1][0] == "b":
                        moves.append(Move((r,c), (r-1, c-1), self.board))
                if c+1<=7:
                    if self.board[r-1][c+1][0] == "b":
                        moves.append(Move((r,c), (r-1, c+1), self.board))
        else:
            if r+1 < len(self.board):    
                if self.board[r+1][c] == "__":
                    moves.append(Move((r,c), (r+1, c), self.board))
                    if r == 1 and self.board[r+2][c] == "__":
                        moves.append(Move((r,c), (r+2, c), self.board))
                if c-1>=0 :
                    if self.board[r+1][c-1][0] == "w":
                        moves.append(Move((r,c), (r+1, c-1), self.board))
                if c+1<=7:
                    if self.board[r+1][c+1][0] == "w":
                        moves.append(Move((r,c), (r+1, c+1), self.board))
        
            
                            
    def getRookMoves(self, r, c, moves):              
        # up
        for i in range(8):
            if r-i >= 0 and r-i!=r:
                if self.board[r-i][c] == "__":
                    moves.append(Move((r,c), (r-i, c), self.board))
                elif self.board[r-i][c][0] == "b" and self.whiteToMove or self.board[r-i][c][0] == "w" and not self.whiteToMove:
                    moves.append(Move((r,c), (r-i, c), self.board))
                    break
                elif self.board[r-i][c][0] == "w" and self.whiteToMove or self.board[r-i][c][0] == "b" and not self.whiteToMove:
                    break
        # down
        for i in range(8):
            if r+i <= 7 and r+i!=r:
                if self.board[r+i][c] == "__":
                    moves.append(Move((r,c), (r+i, c), self.board))
                elif self.board[r+i][c][0] == "b" and self.whiteToMove or self.board[r+i][c][0] == "w" and not self.whiteToMove:
                    moves.append(Move((r,c), (r+i, c), self.board))
                    break
                elif self.board[r+i][c][0] == "w" and self.whiteToMove or self.board[r+i][c][0] == "b" and not self.whiteToMove:
                    break
        # right
        for i in range(8):
            if c+i <= 7 and c+i!=c:
                if self.board[r][c+i] == "__":
                    moves.append(Move((r,c), (r, c+i), self.board))
                elif self.board[r][c+i][0] == "b" and self.whiteToMove or self.board[r][c+i][0] == "w" and not self.whiteToMove:
                    moves.append(Move((r,c), (r, c+i), self.board))
                    break
                elif self.board[r][c+i][0] == "w" and self.whiteToMove or self.board[r][c+i][0] == "b" and not self.whiteToMove:
                    break
        # left
        for i in range(8):
            if c-i >= 0 and c-i!=c:
                if self.board[r][c-i] == "__":
                    moves.append(Move((r,c), (r, c-i), self.board))
                elif self.board[r][c-i][0] == "b" and self.whiteToMove or self.board[r][c-i][0] == "w" and not self.whiteToMove:
                    moves.append(Move((r,c), (r, c-i), self.board))
                    break
                elif self.board[r][c-i][0] == "w" and self.whiteToMove or self.board[r][c-i][0] == "b" and not self.whiteToMove:
                    break
      
    def getKnightMoves(self, r, c, moves):              
        if c+2 <= 7:
            if r+1 <= 7:
                if self.board[r+1][c+2] == "__" or self.board[r+1][c+2][0] == "b" and self.whiteToMove or  self.board[r+1][c+2][0] == "w"and not self.whiteToMove:
                    moves.append(Move((r,c), (r+1, c+2), self.board))
            if r-1 >= 0:
                if self.board[r-1][c+2] == "__" or self.board[r-1][c+2][0] == "b" and self.whiteToMove or  self.board[r-1][c+2][0] == "w"and not self.whiteToMove:
                    moves.append(Move((r,c), (r-1, c+2), self.board))
        
        if c-2 >= 0:
            if r+1 <= 7:
                if self.board[r+1][c-2] == "__" or self.board[r+1][c-2][0] == "b" and self.whiteToMove or  self.board[r+1][c-2][0] == "w"and not self.whiteToMove:
                    moves.append(Move((r,c), (r+1, c-2), self.board))
            if r-1 >= 0:
                if self.board[r-1][c-2] == "__" or self.board[r-1][c-2][0] == "b" and self.whiteToMove or  self.board[r-1][c-2][0] == "w"and not self.whiteToMove:
                    moves.append(Move((r,c), (r-1, c-2), self.board))
        
        if r+2 <= 7:
            if c+1 <= 7:
                if self.board[r+2][c+1] == "__" or self.board[r+2][c+1][0] == "b" and self.whiteToMove or  self.board[r+2][c+1][0] == "w"and not self.whiteToMove:
                    moves.append(Move((r,c), (r+2, c+1), self.board))
            if c-1 >= 0:
                if self.board[r+2][c-1] == "__" or self.board[r+2][c-1][0] == "b" and self.whiteToMove or  self.board[r+2][c-1][0] == "w"and not self.whiteToMove:
                    moves.append(Move((r,c), (r+2, c-1), self.board))
        
        if r-2 >= 0:
            if c+1 <= 7:
                if self.board[r-2][c+1] == "__" or self.board[r-2][c+1][0] == "b" and self.whiteToMove or  self.board[r-2][c+1][0] == "w"and not self.whiteToMove:
                    moves.append(Move((r,c), (r-2, c+1), self.board))
            if c-1 >= 0:
                if self.board[r-2][c-1] == "__" or self.board[r-2][c-1][0] == "b" and self.whiteToMove or  self.board[r-2][c-1][0] == "w"and not self.whiteToMove:
                    moves.append(Move((r,c), (r-2, c-1), self.board))
                

    def getBishopMoves(self, r, c, moves):
        ur=1
        ul=1
        dl=1
        dr=1
        for i in range(1, 7, 1):
            if r+i <= 7 and c+i<= 7 and ur:
                if self.board[r+i][c+i] == "__":
                    moves.append(Move((r,c), (r+i, c+i), self.board))
                elif self.board[r+i][c+i][0] == "b" and self.whiteToMove or self.board[r+i][c+i][0] == "w" and not self.whiteToMove:
                    moves.append(Move((r,c), (r+i, c+i), self.board))
                    ur = 0
                elif self.board[r+i][c+i][0] == "b" and not self.whiteToMove or self.board[r+i][c+i][0] == "w" and self.whiteToMove:
                    ur = 0
                    
            if r+i <= 7 and c-i>=0 and ul:
                if self.board[r+i][c-i] == "__":
                    moves.append(Move((r,c), (r+i, c-i), self.board))
                elif self.board[r+i][c-i][0] == "b" and self.whiteToMove or self.board[r+i][c-i][0] == "w" and not self.whiteToMove:
                    moves.append(Move((r,c), (r+i, c-i), self.board))
                    ul = 0
                elif self.board[r+i][c-i][0] == "b" and not self.whiteToMove or self.board[r+i][c-i][0] == "w" and self.whiteToMove:
                    ul = 0
                    
            if r-i >= 0 and c+i<= 7 and dr:
                if self.board[r-i][c+i] == "__":
                    moves.append(Move((r,c), (r-i, c+i), self.board))
                elif self.board[r-i][c+i][0] == "b" and self.whiteToMove or self.board[r-i][c+i][0] == "w" and not self.whiteToMove:
                    moves.append(Move((r,c), (r-i, c+i), self.board))
                    dr = 0
                elif self.board[r-i][c+i][0] == "b" and not self.whiteToMove or self.board[r-i][c+i][0] == "w" and self.whiteToMove:
                    dr = 0
                    
            if r-i >= 0 and c-i>=0 and dl:
                if self.board[r-i][c-i] == "__":
                    moves.append(Move((r,c), (r-i, c-i), self.board))
                elif self.board[r-i][c-i][0] == "b" and self.whiteToMove or self.board[r-i][c-i][0] == "w" and not self.whiteToMove:
                    moves.append(Move((r,c), (r-i, c-i), self.board))
                    dl = 0
                elif self.board[r-i][c-i][0] == "b" and not self.whiteToMove or self.board[r-i][c-i][0] == "w" and self.whiteToMove:
                    dl = 0

    def getQueenMoves(self, r, c, moves):              
        self.getRookMoves(r, c, moves)
        self.getBishopMoves(r, c, moves)
        
                
    def getKingMoves(self, r, c, moves):              
        rows = [0, 0, 1, -1, 1, 1, -1, -1]
        cols = [1, -1, 0, 0, 1, -1, 1, -1]
        
        for i, j in zip(rows, cols):
             if r+i >= 0 and r+i <= 7 and c+i <= 7 and c+i >= 0:
                if self.board[r+i][c+j] == "__":
                    moves.append(Move((r,c), (r+i, c+j), self.board))
                elif self.board[r+i][c+j][0] == "b" and self.whiteToMove or self.board[r+i][c+j][0] == "w" and not self.whiteToMove:
                    moves.append(Move((r,c), (r+i, c+j), self.board))
        
class Move():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowToRanks = {v:k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, 
                   "e": 4, "f": 5, "g": 6, "h":7}
    colsToFiles = {v:k for k, v in filesToCols.items()}
    
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveId = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol
    
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveId == other.moveId
        return False
    
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    
    def getRankFile(self,r ,c):
        return self.colsToFiles[c] + self.rowToRanks[r] 

