import MoveFunctions
from checks import isCheck
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
        if  isCheck(gs, ally):
            toBeRemoved = []
            for move in moves:
                self.makeMove(move)
                if isCheck(gs, ally):
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

          
            
            
        
                
