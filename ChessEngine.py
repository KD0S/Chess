import MoveFunctions
from Move import Move

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
        self.moveFunctions = {"p": MoveFunctions.getPawnMoves, "R": MoveFunctions.getRookMoves,
                              "N": MoveFunctions.getKnightMoves, "B": MoveFunctions.getBishopMoves,
                              "K": MoveFunctions.getKingMoves, "Q": MoveFunctions.getQueenMoves}
        self.whiteKingLocation = (7, 4)
        self.blackKingLocation = (0, 4)
        self.whiteCheck = False
        self.blackCheck = False
        
    def makeMove(self, move):
        if move.pieceMoved == '__':
            pass
        else:
            self.board[move.startRow][move.startCol] = '__'
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moveLogs.append(move)
            self.whiteToMove = not self.whiteToMove
            if move.pieceMoved == "wK":
                self.whiteKingLocation = (move.endRow, move.endCol)
            elif move.pieceMoved == "bK":
                self.blackKingLocation = (move.endRow, move.endCol)
            
    
    def undoMove(self):
        if len(self.moveLogs) != 0:
            move = self.moveLogs.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
            if move.pieceMoved == "wK":
                self.whiteKingLocation = (move.startRow, move.startCol)
            elif move.pieceMoved == "bK":
                self.blackKingLocation = (move.startRow, move.startCol)
    
    def getValidMoves(self, gs):
        moves = self.getAllPossibleMoves(gs)
        if self.whiteToMove:
            ally = "w"
        else:
            ally = "b"
        check = False
        if self.isCheck(ally):
            toBeRemoved = []
            for move in moves:
                self.makeMove(move)
                if self.isCheck(ally):
                    toBeRemoved.append(move)
                self.undoMove()
            for move in toBeRemoved:
                moves.remove(move)
        if (len(moves) == 0):
            print("CheckMate! Press Z to undo moves")
        return moves
    
    def getAllPossibleMoves(self, gs):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](gs, r, c, moves)
        return moves
                        
    def displayPossibleMoves(self, r, c, moves):
        cells_to_be_highlighted = []
        for move in moves:
            if (r, c) == (move.startRow, move.startCol):
                cells_to_be_highlighted.append((move.endRow, move.endCol))
        return cells_to_be_highlighted
    
    def isCheck(self, ally):        
        # get king square
        if ally == 'w':  
            (Kr, Kc) = self.whiteKingLocation
        else:
            (Kr, Kc) = self.blackKingLocation
            
        # Check for Pawn
        if ally == 'b':
            if Kr+1 <= 7 and Kc+1 <= 7 and self.board[Kr+1][Kc+1][0] != ally:
                if self.board[Kr+1][Kc+1][1] == 'p':
                    return True
            
            if Kr+1 <= 7 and Kc-1 >= 0 and self.board[Kr+1][Kc-1][0] != ally:
                if self.board[Kr+1][Kc-1][1] == 'p':
                    return True
        else:
            if Kr-1 >= 0 and Kc+1 <= 7 and self.board[Kr-1][Kc+1][0] != ally:
                if self.board[Kr-1][Kc+1][1] == 'p':
                    return True
            
            if Kr-1 >= 0 and Kc-1 >= 0 and self.board[Kr-1][Kc-1][0] != ally:
                if self.board[Kr-1][Kc-1][1] == 'p':
                    return True
        
        # Check for Knight
        if Kr+2 <= 7 and Kc+1 <= 7 and self.board[Kr+2][Kc+1][0] != ally:
            if self.board[Kr+2][Kc+1][1] == 'N':
                return True
        
        if Kr+2 <= 7 and Kc-1 >= 0 and self.board[Kr+2][Kc-1][0] != ally:
            if self.board[Kr+2][Kc-1][1] == 'N':
                return True
        
        if Kr+1 <= 7 and Kc+2 <= 7 and self.board[Kr+1][Kc+2][0] != ally:
            if self.board[Kr+1][Kc+2][1] == 'N':
                return True
        
        if Kr+1 <= 7 and Kc-2 >= 0 and self.board[Kr+1][Kc-2][0] != ally:
            if self.board[Kr+1][Kc-2][1] == 'N':
                return True
        
        if Kr-2 >= 0 and Kc+1 <= 7 and self.board[Kr-2][Kc+1][0] != ally:
            if self.board[Kr-2][Kc+1][1] == 'N':
                return True
        
        if Kr-2 >= 0 and Kc-1 >= 0 and self.board[Kr-2][Kc-1][0] != ally:
            if self.board[Kr-2][Kc-1][1] == 'N':
                return True
        
        if Kr-1 >= 0 and Kc+2 <= 7 and self.board[Kr-1][Kc+2][0] != ally:
            if self.board[Kr-1][Kc+2][1] == 'N':
                return True
        
        if Kr-1 >= 0 and Kc-2 >= 0 and self.board[Kr-1][Kc-2][0] != ally:
            if self.board[Kr-1][Kc-2][1] == 'N':
                return True
        
        # Check for King
        rows = [0, 0, 1, -1, 1, 1, -1, -1]
        cols = [1, -1, 0, 0, 1, -1, 1, -1]
        
        for i, j in zip(rows, cols):
            if Kr+i >= 0 and Kc+j >= 0 and Kr+i <= 7 and Kc+j <= 7:
                if self.board[Kr+i][Kc+j][0] != ally and self.board[Kr+i][Kc+j][1] == 'K':
                    return True
        
        # Check for Rook, Queen
        for i in range(1, 7, 1):
            if Kr+i <= 7:
                if self.board[Kr+i][Kc][0] == ally:
                    break
                elif self.board[Kr+i][Kc][1] == 'R' or self.board[Kr+i][Kc][1] == 'Q':
                    return True
                elif self.board[Kr+i][Kc][0] != '_' and self.board[Kr+i][Kc][1] != 'R' and self.board[Kr+i][Kc][1] != 'Q':
                    break
        
        for i in range(1, 7, 1):
            if Kr-i >= 0:
                if self.board[Kr-i][Kc][0] == ally:
                    break
                elif self.board[Kr-i][Kc][1] == 'R' or self.board[Kr-i][Kc][1] == 'Q':
                    return True
                elif self.board[Kr-i][Kc][0] != '_' and self.board[Kr-i][Kc][1] != 'R' and self.board[Kr-i][Kc][1] != 'Q':
                    break
        
        for i in range(1, 7, 1):
            if Kc+i <= 7:
                if self.board[Kr][Kc+i][0] == ally:
                    break
                elif self.board[Kr][Kc+i][1] == 'R' or self.board[Kr][Kc+i][1] == 'Q':
                    return True
                elif self.board[Kr][Kc+i][0] != '_' and self.board[Kr][Kc+i][1] != 'R' and self.board[Kr][Kc+i][1] != 'Q':
                    break
        
        for i in range(1, 7, 1):
            if Kc-i >= 0:
                if self.board[Kr][Kc-i][0] == ally:
                    break
                elif self.board[Kr][Kc-i][1] == 'R' or self.board[Kr][Kc-i][1] == 'Q':
                    return True
                elif self.board[Kr][Kc-i][0] != '_' and self.board[Kr][Kc-i][1] != 'R' and self.board[Kr][Kc-i][1] != 'Q':
                    break
        
        # Check for Bishop, Queen
        for i in range(1, 7, 1):
            if Kr+i <= 7 and Kc+i <= 7:
                if self.board[Kr+i][Kc+i][0] == ally:
                    break
                elif self.board[Kr+i][Kc+i][1] == 'B' or self.board[Kr+i][Kc+i][1] == 'Q':
                    return True
                elif self.board[Kr+i][Kc+i][0] != '_' and self.board[Kr+i][Kc+i][1] != 'B' and self.board[Kr+i][Kc+i][1] != 'Q':
                    break
        
        for i in range(1, 7, 1):
            if Kr-i >= 0 and Kc+i <= 7:
                if self.board[Kr-i][Kc+i][0] == ally:
                    break
                elif self.board[Kr-i][Kc+i][1] == 'B' or self.board[Kr-i][Kc+i][1] == 'Q':
                    return True
                elif self.board[Kr-i][Kc+i][0] != '_' and self.board[Kr-i][Kc+i][1] != 'B' and self.board[Kr-i][Kc+i][1] != 'Q':
                    break
        
        for i in range(1, 7, 1):
            if Kc-i >= 0 and Kr+i <= 7:
                if self.board[Kr+i][Kc-i][0] == ally:
                    break
                elif self.board[Kr+i][Kc-i][1] == 'B' or self.board[Kr+i][Kc-i][1] == 'Q':
                    return True
                elif self.board[Kr+i][Kc-i][0] != '_' and self.board[Kr+i][Kc-i][1] != 'B' and self.board[Kr+i][Kc-i][1] != 'Q':
                    break
        
        for i in range(1, 7, 1):
            if Kc-i >= 0 and Kr-i >= 0:
                if self.board[Kr-i][Kc-i][0] == ally:
                    break
                elif self.board[Kr-i][Kc-i][1] == 'B' or self.board[Kr-i][Kc-i][1] == 'Q':
                    return True
                elif self.board[Kr-i][Kc-i][0] != '_' and self.board[Kr-i][Kc-i][1] != 'B' and self.board[Kr-i][Kc-i][1] != 'Q':
                    break
        
                

             
          
            
            
        
                
