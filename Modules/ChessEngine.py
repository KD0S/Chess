from Modules.checks import isCheck
from Modules.Move import Move
from Modules.MoveFunctions import (getBishopMoves, getKingMoves, getKnightMoves, 
                            getPawnMoves, getQueenMoves, getRookMoves)
from Modules.FEN import FEN

class GameState():
    def __init__(self, player):
        self.board = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                      ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['__', '__', '__', '__', '__', '__', '__', '__'],
                      ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                      ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        self.player = player
        self.enemy = "b" if player == "w" else "w"
        if player == 'b':
         self.board.reverse()
         for row in self.board:
             row.reverse()
        self.playerToMove = True if player == "w" else False
        self.moveLogs = []
        self.moveFunctions = {"R": getRookMoves, "N": getKnightMoves, 
                              "p": getPawnMoves, "K": getKingMoves,
                              "B": getBishopMoves, "Q": getQueenMoves}
        self.playerKingLocation = (7, 4)
        self.enemyKingLocation = (0, 4)
        self.playerKingMoved = 0
        self.enemyKingMoved = 0
        self.playerCastle = False
        self.enemyCastle = False
        self.boardPieces = {'wK': 1, 'wQ': 1, 'wN': 2, 'wB': 2, 'wR': 2, 'wp': 8,
                            'bK': 1, 'bQ': 1, 'bN': 2, 'bB': 2, 'bR': 2, 'bp': 8}
        self.pieces = ["K", "Q", "R", "B", "N", "p"]
        self.inSuffiecientMaterial = False
        self.insuffientMaterialCombinations = [
            # K v K 
            {'wK': 1, 'wQ': 0, 'wN': 0, 'wB': 0, 'wR': 0, 'wp': 0,
            'bK': 1, 'bQ': 0, 'bN': 0, 'bB': 0, 'bR': 0, 'bp': 0}, 
            
            # N+K v K
            {'wK': 1, 'wQ': 0, 'wN': 1, 'wB': 0, 'wR': 0, 'wp': 0,
            'bK': 1, 'bQ': 0, 'bN': 0, 'bB': 0, 'bR': 0, 'bp': 0},
            
            {'wK': 1, 'wQ': 0, 'wN': 0, 'wB': 0, 'wR': 0, 'wp': 0,
            'bK': 1, 'bQ': 0, 'bN': 1, 'bB': 0, 'bR': 0, 'bp': 0},
            
            # B+K v K
            {'wK': 1, 'wQ': 0, 'wN': 0, 'wB': 1, 'wR': 0, 'wp': 0,
            'bK': 1, 'bQ': 0, 'bN': 0, 'bB': 0, 'bR': 0, 'bp': 0},
            
            {'wK': 1, 'wQ': 0, 'wN': 0, 'wB': 0, 'wR': 0, 'wp': 0,
            'bK': 1, 'bQ': 0, 'bN': 0, 'bB': 1, 'bR': 0, 'bp': 0}]
        self.stateLogs = []
        self.FEN = FEN()
        self.threeFoldRepition = False
        
    def makeMove(self, move):
        if move.pieceMoved == '__':
            pass
        else:
            #en-passant
            if move.pieceMoved == self.player+"p" and move.enPassant:
                self.board[move.endRow+1][move.endCol] = "__"

            elif move.pieceMoved == self.enemy+"p" and move.enPassant:
                self.board[move.endRow-1][move.endCol] = "__"

            self.moveLogs.append(move)
            
            self.board[move.startRow][move.startCol] = '__'
            self.board[move.endRow][move.endCol] = move.pieceMoved

            # right-Castling
            if move.pieceMoved == self.player+"K" and move.endCol == move.startCol+2:
                move1 = Move((7, 7), (7, move.endCol-1), self.board)
                self.board[7][7] = '__'
                self.board[7][move.endCol-1] = self.player+"R"
                self.playerCastle = True
                move.ksCastling = True
                self.moveLogs.append(move1)
            elif move.pieceMoved == self.enemy+"K" and move.endCol == move.startCol+2:
                move1 = Move((0, 7), (0, move.endCol-1), self.board)
                self.board[0][7] = '__'
                self.board[0][move.endCol-1] = self.enemy+"R"
                self.enemyCastle = True
                move.ksCastling = True
                self.moveLogs.append(move1)

            # Left-Castling
            if move.pieceMoved == self.player+"K" and move.endCol == move.startCol-2:
                move1 = Move((7, 0), (7, move.endCol+1), self.board)
                self.board[7][0] = '__'
                self.board[7][move.endCol+1] = self.player+"R"
                self.playerCastle = True
                move.qsCastling = True
                self.moveLogs.append(move1)
                
            elif move.pieceMoved == self.enemy+"K" and move.endCol == move.startCol-2:
                move1 = Move((0, 0), (0, move.endCol+1), self.board)
                self.board[0][7] = '__'
                self.board[0][move.endCol+1] = self.enemy+"R"
                self.enemyCastle = True
                move.qsCastling = True
                self.moveLogs.append(move1)
            
            if move.pieceCaptured != "__":
                self.boardPieces[move.pieceCaptured]-=1
            
            self.playerToMove = not self.playerToMove
            
            # Check for 3-Fold Repitition
            boardNotation = self.FEN.positionTOFEN(self.board)
            
            currState = {'playerCastle': self.playerCastle,
                         'enemyCastle': self.enemyCastle, #'moves': len(moves), 
                         'playerToMove': self.playerToMove}

            positionState = {boardNotation : currState}
            
            if positionState in self.stateLogs:
                if self.stateLogs.count(positionState) == 2:
                    self.threeFoldRepition = True
        
            self.stateLogs.append(positionState)
            
            if move.pieceMoved == self.player+"K":
                self.playerKingLocation = (move.endRow, move.endCol)
                self.playerKingMoved+=1

            if move.pieceMoved == self.enemy+"K":
                self.enemyKingLocation = (move.endRow, move.endCol)
                self.enemyKingMoved+=1

    def undoMove(self):
        if len(self.moveLogs) != 0:
            move = self.moveLogs.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.playerToMove = not self.playerToMove

            if move.enPassant:
                if self.playerToMove:
                    self.board[move.endRow+1][move.endCol] = self.enemy+"p"
                else:
                    self.board[move.endRow-1][move.endCol] = self.player+"p"

            #Left-Castling
            if move.pieceMoved == self.player+"R" and move.endCol == self.playerKingLocation[1]-1:
                move1 = self.moveLogs[-1]
                if move1.pieceMoved == self.player+"K" and move1.endCol == move1.startCol+2:
                    move = self.moveLogs.pop()
                    self.playerCastle = False
                    self.board[move.startRow][move.startCol] = move.pieceMoved
                    self.board[move.endRow][move.endCol] = move.pieceCaptured
            elif move.pieceMoved == self.enemy+"R" and move.endCol == self.enemyKingLocation[1]-1:
                move1 = self.moveLogs[-1]
                if move1.pieceMoved == self.enemy+"K" and move1.endCol == move1.startCol+2:
                    move = self.moveLogs.pop()
                    self.enemyCastle = False
                    self.board[move.startRow][move.startCol] = move.pieceMoved
                    self.board[move.endRow][move.endCol] = move.pieceCaptured

            #Right-Castling
            if move.pieceMoved == self.player+"R" and move.endCol == self.playerKingLocation[1]+1:
                move1 = self.moveLogs[-1]
                if move1.pieceMoved == self.player+"K" and move1.endCol == move1.startCol-2:
                    move = self.moveLogs.pop()
                    self.playerCastle = False
                    self.board[move.startRow][move.startCol] = move.pieceMoved
                    self.board[move.endRow][move.endCol] = move.pieceCaptured
            elif move.pieceMoved == self.enemy+"R" and move.endCol == self.enemyKingLocation[1]+1:
                move1 = self.moveLogs[-1]
                if move1.pieceMoved == self.enemy+"K" and move1.endCol == move1.startCol-2:
                    move = self.moveLogs.pop()
                    self.enemyCastle = False
                    self.board[move.startRow][move.startCol] = move.pieceMoved
                    self.board[move.endRow][move.endCol] = move.pieceCaptured
            
            self.stateLogs.pop()

            if move.pieceCaptured != "__":
                self.boardPieces[move.pieceCaptured]+=1
            
            if move.pieceMoved == self.player+"K":
                self.playerKingLocation = (move.startRow, move.startCol)
                self.playerKingMoved-=1

            if move.pieceMoved == self.enemy+"K":
                self.enemyKingLocation = (move.startRow, move.startCol)
                self.enemyKingMoved-=1
    
    def getValidMoves(self):
        moves = self.getAllPossibleMoves()
        
        if self.boardPieces in self.insuffientMaterialCombinations:
            self.inSuffiecientMaterial = True
            return []
        
        if self.threeFoldRepition:
            return []
        
        if self.playerToMove:
            ally = self.player
        else:
            ally = self.enemy
            
        toBeRemoved = []
        for move in moves:
            self.makeMove(move)
            (Kr, Kc) = self.getKingLocation(ally)
            if isCheck(self.board, ally, self.player, Kr, Kc):
                toBeRemoved.append(move)
            self.undoMove()
        for move in toBeRemoved:
            moves.remove(move)
        
        return moves

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (self.playerToMove and self.player == turn 
                    or not self.playerToMove and self.enemy == turn):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](self, r, c, moves)
        return moves

    def displayPossibleMoves(self, r, c, moves):
        cells_to_be_highlighted = []
        for move in moves:
            if (r, c) == (move.startRow, move.startCol):
                cells_to_be_highlighted.append((move.endRow, move.endCol))
        return cells_to_be_highlighted

    def getKingLocation(self, ally):
        if ally == self.player:
            (Kr, Kc) = self.playerKingLocation
        else:
            (Kr, Kc) = self.enemyKingLocation

        return (Kr, Kc)
    
