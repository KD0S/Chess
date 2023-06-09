from Move import Move
from checks import isCheck

def getPawnMoves(gs, r, c, moves, player):
    if gs.playerToMove:
        enemy = "w" if player == "b" else "b"
        if r-1>=0:
            if gs.board[r-1][c] == "__":
                moves.append(Move((r,c), (r-1, c), gs.board))
                if r == 6 and gs.board[r-2][c] == "__":
                    moves.append(Move((r,c), (r-2, c), gs.board))
            if c-1>=0:
                if gs.board[r-1][c-1][0] == enemy:
                    moves.append(Move((r,c), (r-1, c-1), gs.board))
            if c+1<=7:
                if gs.board[r-1][c+1][0] == enemy:
                    moves.append(Move((r,c), (r-1, c+1), gs.board))
                    
        # check for en-passant
        if len(gs.moveLogs) > 0:
            move = gs.moveLogs[-1]
            if move.pieceMoved == gs.enemy+"p" and move.endRow == move.startRow+2:
                pr, pc = move.endRow, move.endCol
                if r == pr and ((c+1 <= 7 and pc == c+1) or (c-1 >= 0 and pc == c-1)):
                    move = Move((r,c), (r-1, pc), gs.board)
                    moves.append(move)
            
    else:
        if r+1 < len(gs.board):    
            if gs.board[r+1][c] == "__":
                moves.append(Move((r,c), (r+1, c), gs.board))
                if r == 1 and gs.board[r+2][c] == "__":
                    moves.append(Move((r,c), (r+2, c), gs.board))
            if c-1>=0 :
                if gs.board[r+1][c-1][0] == player:
                    moves.append(Move((r,c), (r+1, c-1), gs.board))
            if c+1<=7:
                if gs.board[r+1][c+1][0] == player:
                    moves.append(Move((r,c), (r+1, c+1), gs.board))
            
              # check for en-passant
            if len(gs.moveLogs) > 0:
                move = gs.moveLogs[-1]
                if move.pieceMoved == gs.player+"p" and move.endRow == move.startRow-2:
                    pr, pc = move.endRow, move.endCol
                    if r == pr and ((c+1 <= 7 and pc == c+1) or (c-1 >= 0 and pc == c-1)):
                        move = Move((r,c), (pr+1, pc), gs.board)
                        moves.append(move)
        
                        
def getRookMoves(gs, r, c, moves, player):              
    # up
    for i in range(8):
        if r-i >= 0 and r-i!=r:
            if gs.board[r-i][c] == "__":
                moves.append(Move((r,c), (r-i, c), gs.board))
            elif gs.board[r-i][c][0] != player and gs.playerToMove or gs.board[r-i][c][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r-i, c), gs.board))
                break
            elif gs.board[r-i][c][0] == player and gs.playerToMove or gs.board[r-i][c][0] != player and not gs.playerToMove:
                break
    # down
    for i in range(8):
        if r+i <= 7 and r+i!=r:
            if gs.board[r+i][c] == "__":
                moves.append(Move((r,c), (r+i, c), gs.board))
            elif gs.board[r+i][c][0] != player and gs.playerToMove or gs.board[r+i][c][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r+i, c), gs.board))
                break
            elif gs.board[r+i][c][0] == player and gs.playerToMove or gs.board[r+i][c][0] != player and not gs.playerToMove:
                break
    # right
    for i in range(8):
        if c+i <= 7 and c+i!=c:
            if gs.board[r][c+i] == "__":
                moves.append(Move((r,c), (r, c+i), gs.board))
            elif gs.board[r][c+i][0] != player and gs.playerToMove or gs.board[r][c+i][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r, c+i), gs.board))
                break
            elif gs.board[r][c+i][0] == player and gs.playerToMove or gs.board[r][c+i][0] != player and not gs.playerToMove:
                break
    # left
    for i in range(8):
        if c-i >= 0 and c-i!=c:
            if gs.board[r][c-i] == "__":
                moves.append(Move((r,c), (r, c-i), gs.board))
            elif gs.board[r][c-i][0] != player and gs.playerToMove or gs.board[r][c-i][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r, c-i), gs.board))
                break
            elif gs.board[r][c-i][0] == player and gs.playerToMove or gs.board[r][c-i][0] != player and not gs.playerToMove:
                break
    
def getKnightMoves(gs, r, c, moves, player):              
    if c+2 <= 7:
        if r+1 <= 7:
            if gs.board[r+1][c+2] == "__" or gs.board[r+1][c+2][0] != player and gs.playerToMove or  gs.board[r+1][c+2][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r+1, c+2), gs.board))
        if r-1 >= 0:
            if gs.board[r-1][c+2] == "__" or gs.board[r-1][c+2][0] != player and gs.playerToMove or  gs.board[r-1][c+2][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r-1, c+2), gs.board))
    
    if c-2 >= 0:
        if r+1 <= 7:
            if gs.board[r+1][c-2] == "__" or gs.board[r+1][c-2][0] != player and gs.playerToMove or  gs.board[r+1][c-2][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r+1, c-2), gs.board))
        if r-1 >= 0:
            if gs.board[r-1][c-2] == "__" or gs.board[r-1][c-2][0] != player and gs.playerToMove or  gs.board[r-1][c-2][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r-1, c-2), gs.board))
    
    if r+2 <= 7:
        if c+1 <= 7:
            if gs.board[r+2][c+1] == "__" or gs.board[r+2][c+1][0] != player and gs.playerToMove or  gs.board[r+2][c+1][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r+2, c+1), gs.board))
        if c-1 >= 0:
            if gs.board[r+2][c-1] == "__" or gs.board[r+2][c-1][0] != player and gs.playerToMove or  gs.board[r+2][c-1][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r+2, c-1), gs.board))
    
    if r-2 >= 0:
        if c+1 <= 7:
            if gs.board[r-2][c+1] == "__" or gs.board[r-2][c+1][0] != player and gs.playerToMove or  gs.board[r-2][c+1][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r-2, c+1), gs.board))
        if c-1 >= 0:
            if gs.board[r-2][c-1] == "__" or gs.board[r-2][c-1][0] != player and gs.playerToMove or  gs.board[r-2][c-1][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r-2, c-1), gs.board))
            

def getBishopMoves(gs, r, c, moves, player):
    ur=1
    ul=1
    dl=1
    dr=1
    for i in range(1, 7, 1):
        if r+i <= 7 and c+i<= 7 and ur:
            if gs.board[r+i][c+i] == "__":
                moves.append(Move((r,c), (r+i, c+i), gs.board))
            elif gs.board[r+i][c+i][0] != player and gs.playerToMove or gs.board[r+i][c+i][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r+i, c+i), gs.board))
                ur = 0
            elif gs.board[r+i][c+i][0] != player and not gs.playerToMove or gs.board[r+i][c+i][0] == player and gs.playerToMove:
                ur = 0
                
        if r+i <= 7 and c-i>=0 and ul:
            if gs.board[r+i][c-i] == "__":
                moves.append(Move((r,c), (r+i, c-i), gs.board))
            elif gs.board[r+i][c-i][0] != player and gs.playerToMove or gs.board[r+i][c-i][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r+i, c-i), gs.board))
                ul = 0
            elif gs.board[r+i][c-i][0] != player and not gs.playerToMove or gs.board[r+i][c-i][0] == player and gs.playerToMove:
                ul = 0
                
        if r-i >= 0 and c+i<= 7 and dr:
            if gs.board[r-i][c+i] == "__":
                moves.append(Move((r,c), (r-i, c+i), gs.board))
            elif gs.board[r-i][c+i][0] != player and gs.playerToMove or gs.board[r-i][c+i][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r-i, c+i), gs.board))
                dr = 0
            elif gs.board[r-i][c+i][0] != player and not gs.playerToMove or gs.board[r-i][c+i][0] == player and gs.playerToMove:
                dr = 0
                
        if r-i >= 0 and c-i>=0 and dl:
            if gs.board[r-i][c-i] == "__":
                moves.append(Move((r,c), (r-i, c-i), gs.board))
            elif gs.board[r-i][c-i][0] != player and gs.playerToMove or gs.board[r-i][c-i][0] == player and not gs.playerToMove:
                moves.append(Move((r,c), (r-i, c-i), gs.board))
                dl = 0
            elif gs.board[r-i][c-i][0] != player and not gs.playerToMove or gs.board[r-i][c-i][0] == player and gs.playerToMove:
                dl = 0

def getQueenMoves(gs, r, c, moves, player):              
    getRookMoves(gs, r, c, moves, player)
    getBishopMoves(gs, r, c, moves, player)

def getKingMoves(gs, r, c, moves, player):              
        rows = [0, 0, 1, -1, 1, 1, -1, -1]
        cols = [1, -1, 0, 0, 1, -1, 1, -1]
        
        kingMoves = []
        
        for i, j in zip(rows, cols):
             if r+i >= 0 and r+i <= 7 and c+j <= 7 and c+j >= 0:
                if gs.board[r+i][c+j] == "__":
                    kingMoves.append(Move((r,c), (r+i, c+j), gs.board))
                elif gs.board[r+i][c+j][0] != player and gs.playerToMove or gs.board[r+i][c+j][0] == player and not gs.playerToMove:
                    kingMoves.append(Move((r,c), (r+i, c+j), gs.board))
                    
        if gs.playerToMove:
            ally = player
        else: 
            ally = "w" if player == "b" else "b"
        toBeRemoved = []
        for move in kingMoves:
            gs.makeMove(move)
            (Kr, Kc) = gs.getKingLocation(ally)
            if isCheck(gs, ally, player, Kr, Kc):
                toBeRemoved.append(move)
            gs.undoMove()
        for move in toBeRemoved:
            kingMoves.remove(move)            
        for move in kingMoves:
            moves.append(move)

        # Left-Castling
        if c+1 <= 7 and c+2 <= 7 and gs.board[r][c+1] == gs.board[r][c+2] == "__":
            if gs.playerToMove and not gs.playerCastle:
                if not isCheck(gs, gs.player, player, r, c):
                    if gs.playerKingMoved==0:
                        KSRook = True
                        for move in gs.moveLogs:
                            if move.pieceMoved == gs.player+"R" and move.startRow == move.startCol == 7 or (
                            move.pieceCaptured == gs.player+"R" and move.endRow == move.endCol == 7):
                                KSRook = False
                                break
                        if KSRook:
                            checkLeftCastleMoves(gs, gs.player, player, r, c, moves)

            
            elif not gs.playerToMove and not gs.enemyCastle:
                if not isCheck(gs, gs.enemy, player, r, c):
                    if gs.enemyKingMoved==0:
                        KSRook = True
                        for move in gs.moveLogs:
                            if move.pieceMoved == gs.enemy+"R" and move.startRow == 0 and move.startCol == 7 or (
                            move.pieceCaptured == gs.enemy+"R" and move.endRow == 0 and move.endCol == 7):
                                KSRook = False
                                break
                        if KSRook:
                            checkLeftCastleMoves(gs, gs.enemy, player, r, c, moves)   
            
        # Right-Castling            
        if c-1 >= 0 and c-2 >= 0 and c-3 >= 0 and gs.board[r][c-1] == gs.board[r][c-2] == gs.board[r][c-3] == "__":
            if gs.playerToMove and not gs.playerCastle:
                if gs.playerKingMoved==0:
                    QSRook = True
                    for move in gs.moveLogs:
                        if move.pieceMoved == gs.player+"R" and move.startRow == 7 and move.startCol == 0 or (
                        move.pieceCaptured == gs.player+"R" and move.endRow == 7 and  move.endCol == 0):
                            QSRook = False
                            break
                    if QSRook:
                        checkRightCastleMoves(gs, gs.player, player, r, c, moves)
                    
            elif not gs.playerToMove and not gs.enemyCastle:
                if gs.enemyKingMoved==0:
                    QSRook = True
                    for move in gs.moveLogs:
                        if move.pieceMoved == gs.enemy+"R" and move.startRow == move.startCol == 0 or (
                        move.pieceCaptured == gs.enemy+"R" and move.endRow == move.endCol == 0):
                            QSRook = False
                            break
                    if QSRook:
                        checkRightCastleMoves(gs, gs.enemy, player, r, c, moves)

def checkLeftCastleMoves(gs, ally, player, r, c, moves):
        if not isCheck(gs, ally, player, r, c+1):
            if not isCheck(gs, ally, player, r, c+2):
                move = Move((r, c), (r, c+2), gs.board)
                moves.append(move)

def checkRightCastleMoves(gs, ally, player, r, c, moves):
        if not isCheck(gs, ally, player, r, c-1):
            if not isCheck(gs, ally, player, r, c-2):
                move = Move((r, c), (r, c-2), gs.board)
                moves.append(move) 