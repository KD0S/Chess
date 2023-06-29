from Modules.Move import Move
from Modules.checks import isCheck

def getPawnMoves(gs, row, col, moves):
        if gs.playerToMove:
            if row-1>=0:
                if gs.board[row-1][col] == "__":
                    move = Move((row,col), (row-1, col), gs.board)
                    if move.endRow == 0:
                            move.pawnPromotion = True
                    moves.append(move)
                    if row == 6 and gs.board[row-2][col] == "__":
                        moves.append(Move((row,col), (row-2, col), gs.board))
                if col-1>=0:
                    if gs.board[row-1][col-1][0] == gs.enemy:
                        move = Move((row,col), (row-1, col-1), gs.board)
                        if move.endRow == 0:
                            move.pawnPromotion = True
                        moves.append(move)
                if col+1<=7:
                    if gs.board[row-1][col+1][0] == gs.enemy:
                        move = Move((row,col), (row-1, col+1), gs.board)
                        if move.endRow == 0:
                            move.pawnPromotion = True
                        moves.append(move)
            
            # check for en-passant
            if len(gs.moveLogs) > 0:
                move = gs.moveLogs[-1]
                if move.pieceMoved == gs.enemy+"p" and move.endRow == move.startRow+2:
                    pr, pc = move.endRow, move.endCol
                    if row == pr and ((col+1 <= 7 and pc == col+1) or (col-1 >= 0 and pc == col-1)):
                        move = Move((row,col), (row-1, pc), gs.board)
                        move.enPassant = True
                        moves.append(move)
            
        else:
            if row+1 < len(gs.board):    
                if gs.board[row+1][col] == "__":
                    move = Move((row,col), (row+1, col), gs.board)
                    if move.endRow == 7:
                        move.pawnPromotion = True
                    moves.append(move)
                    if row == 1 and gs.board[row+2][col] == "__":
                        moves.append(Move((row,col), (row+2, col), gs.board))
                if col-1>=0 :
                    if gs.board[row+1][col-1][0] == gs.player:
                        move = Move((row,col), (row+1, col-1), gs.board)
                        if move.endRow == 7:
                            move.pawnPromotion = True
                        moves.append(move)
                if col+1<=7:
                    if gs.board[row+1][col+1][0] == gs.player:
                        move = Move((row,col), (row+1, col+1), gs.board)
                        if move.endRow == 7:
                            move.pawnPromotion = True
                        moves.append(move)
                
                # check for en-passant
                if len(gs.moveLogs) > 0:
                    move = gs.moveLogs[-1]
                    if move.pieceMoved == gs.player+"p" and move.endRow == move.startRow-2:
                        pr, pc = move.endRow, move.endCol
                        if row == pr and ((col+1 <= 7 and pc == col+1) or (col-1 >= 0 and pc == col-1)):
                            move = Move((row,col), (pr+1, pc), gs.board)
                            move.enPassant = True
                            moves.append(move)
        
                        
def getRookMoves(gs, row, col, moves):              
    # up
    for i in range(8):
        if row-i >= 0 and row-i!=row:
            if gs.board[row-i][col] == "__":
                moves.append(Move((row,col), (row-i, col), gs.board))
            elif (gs.board[row-i][col][0] != gs.player and gs.playerToMove or 
                    gs.board[row-i][col][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row-i, col), gs.board))
                break
            elif (gs.board[row-i][col][0] == gs.player and gs.playerToMove or 
                    gs.board[row-i][col][0] != gs.player and not gs.playerToMove):
                break
    # down
    for i in range(8):
        if row+i <= 7 and row+i!=row:
            if gs.board[row+i][col] == "__":
                moves.append(Move((row,col), (row+i, col), gs.board))
            elif (gs.board[row+i][col][0] != gs.player and gs.playerToMove 
                    or gs.board[row+i][col][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row+i, col), gs.board))
                break
            elif (gs.board[row+i][col][0] == gs.player and gs.playerToMove 
                    or gs.board[row+i][col][0] != gs.player and not gs.playerToMove):
                break
    # right
    for i in range(8):
        if col+i <= 7 and col+i!=col:
            if gs.board[row][col+i] == "__":
                moves.append(Move((row,col), (row, col+i), gs.board))
            elif (gs.board[row][col+i][0] != gs.player and gs.playerToMove 
                    or gs.board[row][col+i][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row, col+i), gs.board))
                break
            elif (gs.board[row][col+i][0] == gs.player and gs.playerToMove 
                    or gs.board[row][col+i][0] != gs.player and not gs.playerToMove):
                break
    # left
    for i in range(8):
        if col-i >= 0 and col-i!=col:
            if gs.board[row][col-i] == "__":
                moves.append(Move((row,col), (row, col-i), gs.board))
            elif (gs.board[row][col-i][0] != gs.player and gs.playerToMove 
                    or gs.board[row][col-i][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row, col-i), gs.board))
                break
            elif (gs.board[row][col-i][0] == gs.player and gs.playerToMove 
                or gs.board[row][col-i][0] != gs.player and not gs.playerToMove):
                break
    
def getKnightMoves(gs, row, col, moves):              
    if col+2 <= 7:
        if row+1 <= 7:
            if (gs.board[row+1][col+2] == "__" 
            or gs.board[row+1][col+2][0] != gs.player and gs.playerToMove 
            or  gs.board[row+1][col+2][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row+1, col+2), gs.board))
        if row-1 >= 0:
            if (gs.board[row-1][col+2] == "__" 
            or gs.board[row-1][col+2][0] != gs.player and gs.playerToMove 
            or  gs.board[row-1][col+2][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row-1, col+2), gs.board))
    
    if col-2 >= 0:
        if row+1 <= 7:
            if (gs.board[row+1][col-2] == "__" 
            or gs.board[row+1][col-2][0] != gs.player and gs.playerToMove 
            or  gs.board[row+1][col-2][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row+1, col-2), gs.board))
        if row-1 >= 0:
            if (gs.board[row-1][col-2] == "__" 
            or gs.board[row-1][col-2][0] != gs.player and gs.playerToMove 
            or  gs.board[row-1][col-2][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row-1, col-2), gs.board))
    
    if row+2 <= 7:
        if col+1 <= 7:
            if (gs.board[row+2][col+1] == "__" 
            or gs.board[row+2][col+1][0] != gs.player and gs.playerToMove 
            or  gs.board[row+2][col+1][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row+2, col+1), gs.board))
        if col-1 >= 0:
            if (gs.board[row+2][col-1] == "__" 
            or gs.board[row+2][col-1][0] != gs.player and gs.playerToMove 
            or  gs.board[row+2][col-1][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row+2, col-1), gs.board))
    
    if row-2 >= 0:
        if col+1 <= 7:
            if (gs.board[row-2][col+1] == "__" 
                or gs.board[row-2][col+1][0] != gs.player and gs.playerToMove 
                or  gs.board[row-2][col+1][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row-2, col+1), gs.board))
        if col-1 >= 0:
            if (gs.board[row-2][col-1] == "__" 
            or gs.board[row-2][col-1][0] != gs.player and gs.playerToMove 
            or  gs.board[row-2][col-1][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row-2, col-1), gs.board))
            

def getBishopMoves(gs, row, col, moves):
    ur=1
    ul=1
    dl=1
    dr=1
    for i in range(1, 7, 1):
        if row+i <= 7 and col+i<= 7 and ur:
            if gs.board[row+i][col+i] == "__":
                moves.append(Move((row,col), (row+i, col+i), gs.board))
            elif (gs.board[row+i][col+i][0] != gs.player and gs.playerToMove 
                    or gs.board[row+i][col+i][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row+i, col+i), gs.board))
                ur = 0
            elif (gs.board[row+i][col+i][0] != gs.player and not gs.playerToMove 
                    or gs.board[row+i][col+i][0] == gs.player and gs.playerToMove):
                ur = 0
                
        if row+i <= 7 and col-i>=0 and ul:
            if gs.board[row+i][col-i] == "__":
                moves.append(Move((row,col), (row+i, col-i), gs.board))
            elif (gs.board[row+i][col-i][0] != gs.player and gs.playerToMove 
                or gs.board[row+i][col-i][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row+i, col-i), gs.board))
                ul = 0
            elif (gs.board[row+i][col-i][0] != gs.player and not gs.playerToMove 
                or gs.board[row+i][col-i][0] == gs.player and gs.playerToMove):
                ul = 0
                
        if row-i >= 0 and col+i<= 7 and dr:
            if gs.board[row-i][col+i] == "__":
                moves.append(Move((row,col), (row-i, col+i), gs.board))
            elif (gs.board[row-i][col+i][0] != gs.player and gs.playerToMove 
                or gs.board[row-i][col+i][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row-i, col+i), gs.board))
                dr = 0
            elif (gs.board[row-i][col+i][0] != gs.player and not gs.playerToMove 
                or gs.board[row-i][col+i][0] == gs.player and gs.playerToMove):
                dr = 0
                
        if row-i >= 0 and col-i>=0 and dl:
            if gs.board[row-i][col-i] == "__":
                moves.append(Move((row,col), (row-i, col-i), gs.board))
            elif (gs.board[row-i][col-i][0] != gs.player and gs.playerToMove 
                or gs.board[row-i][col-i][0] == gs.player and not gs.playerToMove):
                moves.append(Move((row,col), (row-i, col-i), gs.board))
                dl = 0
            elif (gs.board[row-i][col-i][0] != gs.player and not gs.playerToMove 
                or gs.board[row-i][col-i][0] == gs.player and gs.playerToMove):
                dl = 0

def getQueenMoves(gs, row, col, moves):              
    getRookMoves(gs, row, col, moves)
    getBishopMoves(gs, row, col, moves)

def getKingMoves(gs, row, col, moves):              
        rows = [0, 0, 1, -1, 1, 1, -1, -1]
        cols = [1, -1, 0, 0, 1, -1, 1, -1]
        
        kingMoves = []
        
        for i, j in zip(rows, cols):
            if row+i >= 0 and row+i <= 7 and col+j <= 7 and col+j >= 0:
                if gs.board[row+i][col+j] == "__":
                    kingMoves.append(Move((row,col), (row+i, col+j), gs.board))
                elif (gs.board[row+i][col+j][0] != gs.player and gs.playerToMove 
                    or gs.board[row+i][col+j][0] == gs.player and not gs.playerToMove):
                    kingMoves.append(Move((row,col), (row+i, col+j), gs.board))
                    
        if gs.playerToMove:
            ally = gs.player
        else: 
            ally = "w" if gs.player == "b" else "b"
            
        toBeRemoved = []
        for move in kingMoves:
            gs.makeMove(move)
            (Kr, Kc) = gs.getKingLocation(ally)
            if isCheck(gs.board, ally, gs.player, Kr, Kc):
                toBeRemoved.append(move)
            gs.undoMove()
        for move in toBeRemoved:
            kingMoves.remove(move)            
        for move in kingMoves:
            moves.append(move)

        # Left-Castling
        if col+1 <= 7 and col+2 <= 7 and gs.board[row][col+1] == gs.board[row][col+2] == "__":
            if gs.playerToMove and not gs.playerCastle:
                if not isCheck(gs.board, gs.player, gs.player, row, col):
                    if gs.playerKingMoved==0:
                        KSRook = True
                        for move in gs.moveLogs:
                            if move.pieceMoved == gs.player+"row" and move.startRow == move.startCol == 7 or (
                            move.pieceCaptured == gs.player+"row" and move.endRow == move.endCol == 7):
                                KSRook = False
                                break
                        if KSRook:
                            checkLeftCastleMoves(gs, ally, gs.player, row, col, moves)

            
            elif not gs.playerToMove and not gs.enemyCastle:
                if not isCheck(gs.board, gs.enemy, gs.player, row, col):
                    if gs.enemyKingMoved==0:
                        KSRook = True
                        for move in gs.moveLogs:
                            if move.pieceMoved == gs.enemy+"row" and move.startRow == 0 and move.startCol == 7 or (
                            move.pieceCaptured == gs.enemy+"row" and move.endRow == 0 and move.endCol == 7):
                                KSRook = False
                                break
                        if KSRook:
                            checkLeftCastleMoves(gs, ally, gs.player, row, col, moves)   
            
        # Right-Castling            
        if col-1 >= 0 and col-2 >= 0 and col-3 >= 0 and gs.board[row][col-1] == gs.board[row][col-2] == gs.board[row][col-3] == "__":
            if gs.playerToMove and not gs.playerCastle:
                if gs.playerKingMoved==0:
                    QSRook = True
                    for move in gs.moveLogs:
                        if move.pieceMoved == gs.player+"row" and move.startRow == 7 and move.startCol == 0 or (
                        move.pieceCaptured == gs.player+"row" and move.endRow == 7 and  move.endCol == 0):
                            QSRook = False
                            break
                    if QSRook:
                        checkRightCastleMoves(gs, ally, gs.player, row, col, moves)
                    
            elif not gs.playerToMove and not gs.enemyCastle:
                if gs.enemyKingMoved==0:
                    QSRook = True
                    for move in gs.moveLogs:
                        if move.pieceMoved == gs.enemy+"row" and move.startRow == move.startCol == 0 or (
                        move.pieceCaptured == gs.enemy+"row" and move.endRow == move.endCol == 0):
                            QSRook = False
                            break
                    if QSRook:
                        checkRightCastleMoves(gs, ally, gs.player, row, col, moves)

def checkLeftCastleMoves(gs, ally, player, row, col, moves):
        if not isCheck(gs.board, ally, player, row, col+1):
            if not isCheck(gs.board, ally, player, row, col+2):
                move = Move((row, col), (row, col+2), gs.board)
                move.ksCastling = True
                moves.append(move)

def checkRightCastleMoves(gs, ally, player, row, col, moves):
        if not isCheck(gs.board, ally, player, row, col-1):
            if not isCheck(gs.board, ally, player, row, col-2):
                move = Move((row, col), (row, col-2), gs.board)
                move.qsCastlings = True
                moves.append(move) 