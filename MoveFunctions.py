from Move import Move

def getPawnMoves(gs, r, c, moves):
    if gs.whiteToMove:
        if r-1>=0:    
            if gs.board[r-1][c] == "__":
                moves.append(Move((r,c), (r-1, c), gs.board))
                if r == 6 and gs.board[r-2][c] == "__":
                    moves.append(Move((r,c), (r-2, c), gs.board))
            if c-1>=0:
                if gs.board[r-1][c-1][0] == "b":
                    moves.append(Move((r,c), (r-1, c-1), gs.board))
            if c+1<=7:
                if gs.board[r-1][c+1][0] == "b":
                    moves.append(Move((r,c), (r-1, c+1), gs.board))
    else:
        if r+1 < len(gs.board):    
            if gs.board[r+1][c] == "__":
                moves.append(Move((r,c), (r+1, c), gs.board))
                if r == 1 and gs.board[r+2][c] == "__":
                    moves.append(Move((r,c), (r+2, c), gs.board))
            if c-1>=0 :
                if gs.board[r+1][c-1][0] == "w":
                    moves.append(Move((r,c), (r+1, c-1), gs.board))
            if c+1<=7:
                if gs.board[r+1][c+1][0] == "w":
                    moves.append(Move((r,c), (r+1, c+1), gs.board))
    
        
                        
def getRookMoves(gs, r, c, moves):              
    # up
    for i in range(8):
        if r-i >= 0 and r-i!=r:
            if gs.board[r-i][c] == "__":
                moves.append(Move((r,c), (r-i, c), gs.board))
            elif gs.board[r-i][c][0] == "b" and gs.whiteToMove or gs.board[r-i][c][0] == "w" and not gs.whiteToMove:
                moves.append(Move((r,c), (r-i, c), gs.board))
                break
            elif gs.board[r-i][c][0] == "w" and gs.whiteToMove or gs.board[r-i][c][0] == "b" and not gs.whiteToMove:
                break
    # down
    for i in range(8):
        if r+i <= 7 and r+i!=r:
            if gs.board[r+i][c] == "__":
                moves.append(Move((r,c), (r+i, c), gs.board))
            elif gs.board[r+i][c][0] == "b" and gs.whiteToMove or gs.board[r+i][c][0] == "w" and not gs.whiteToMove:
                moves.append(Move((r,c), (r+i, c), gs.board))
                break
            elif gs.board[r+i][c][0] == "w" and gs.whiteToMove or gs.board[r+i][c][0] == "b" and not gs.whiteToMove:
                break
    # right
    for i in range(8):
        if c+i <= 7 and c+i!=c:
            if gs.board[r][c+i] == "__":
                moves.append(Move((r,c), (r, c+i), gs.board))
            elif gs.board[r][c+i][0] == "b" and gs.whiteToMove or gs.board[r][c+i][0] == "w" and not gs.whiteToMove:
                moves.append(Move((r,c), (r, c+i), gs.board))
                break
            elif gs.board[r][c+i][0] == "w" and gs.whiteToMove or gs.board[r][c+i][0] == "b" and not gs.whiteToMove:
                break
    # left
    for i in range(8):
        if c-i >= 0 and c-i!=c:
            if gs.board[r][c-i] == "__":
                moves.append(Move((r,c), (r, c-i), gs.board))
            elif gs.board[r][c-i][0] == "b" and gs.whiteToMove or gs.board[r][c-i][0] == "w" and not gs.whiteToMove:
                moves.append(Move((r,c), (r, c-i), gs.board))
                break
            elif gs.board[r][c-i][0] == "w" and gs.whiteToMove or gs.board[r][c-i][0] == "b" and not gs.whiteToMove:
                break
    
def getKnightMoves(gs, r, c, moves):              
    if c+2 <= 7:
        if r+1 <= 7:
            if gs.board[r+1][c+2] == "__" or gs.board[r+1][c+2][0] == "b" and gs.whiteToMove or  gs.board[r+1][c+2][0] == "w"and not gs.whiteToMove:
                moves.append(Move((r,c), (r+1, c+2), gs.board))
        if r-1 >= 0:
            if gs.board[r-1][c+2] == "__" or gs.board[r-1][c+2][0] == "b" and gs.whiteToMove or  gs.board[r-1][c+2][0] == "w"and not gs.whiteToMove:
                moves.append(Move((r,c), (r-1, c+2), gs.board))
    
    if c-2 >= 0:
        if r+1 <= 7:
            if gs.board[r+1][c-2] == "__" or gs.board[r+1][c-2][0] == "b" and gs.whiteToMove or  gs.board[r+1][c-2][0] == "w"and not gs.whiteToMove:
                moves.append(Move((r,c), (r+1, c-2), gs.board))
        if r-1 >= 0:
            if gs.board[r-1][c-2] == "__" or gs.board[r-1][c-2][0] == "b" and gs.whiteToMove or  gs.board[r-1][c-2][0] == "w"and not gs.whiteToMove:
                moves.append(Move((r,c), (r-1, c-2), gs.board))
    
    if r+2 <= 7:
        if c+1 <= 7:
            if gs.board[r+2][c+1] == "__" or gs.board[r+2][c+1][0] == "b" and gs.whiteToMove or  gs.board[r+2][c+1][0] == "w"and not gs.whiteToMove:
                moves.append(Move((r,c), (r+2, c+1), gs.board))
        if c-1 >= 0:
            if gs.board[r+2][c-1] == "__" or gs.board[r+2][c-1][0] == "b" and gs.whiteToMove or  gs.board[r+2][c-1][0] == "w"and not gs.whiteToMove:
                moves.append(Move((r,c), (r+2, c-1), gs.board))
    
    if r-2 >= 0:
        if c+1 <= 7:
            if gs.board[r-2][c+1] == "__" or gs.board[r-2][c+1][0] == "b" and gs.whiteToMove or  gs.board[r-2][c+1][0] == "w"and not gs.whiteToMove:
                moves.append(Move((r,c), (r-2, c+1), gs.board))
        if c-1 >= 0:
            if gs.board[r-2][c-1] == "__" or gs.board[r-2][c-1][0] == "b" and gs.whiteToMove or  gs.board[r-2][c-1][0] == "w"and not gs.whiteToMove:
                moves.append(Move((r,c), (r-2, c-1), gs.board))
            

def getBishopMoves(gs, r, c, moves):
    ur=1
    ul=1
    dl=1
    dr=1
    for i in range(1, 7, 1):
        if r+i <= 7 and c+i<= 7 and ur:
            if gs.board[r+i][c+i] == "__":
                moves.append(Move((r,c), (r+i, c+i), gs.board))
            elif gs.board[r+i][c+i][0] == "b" and gs.whiteToMove or gs.board[r+i][c+i][0] == "w" and not gs.whiteToMove:
                moves.append(Move((r,c), (r+i, c+i), gs.board))
                ur = 0
            elif gs.board[r+i][c+i][0] == "b" and not gs.whiteToMove or gs.board[r+i][c+i][0] == "w" and gs.whiteToMove:
                ur = 0
                
        if r+i <= 7 and c-i>=0 and ul:
            if gs.board[r+i][c-i] == "__":
                moves.append(Move((r,c), (r+i, c-i), gs.board))
            elif gs.board[r+i][c-i][0] == "b" and gs.whiteToMove or gs.board[r+i][c-i][0] == "w" and not gs.whiteToMove:
                moves.append(Move((r,c), (r+i, c-i), gs.board))
                ul = 0
            elif gs.board[r+i][c-i][0] == "b" and not gs.whiteToMove or gs.board[r+i][c-i][0] == "w" and gs.whiteToMove:
                ul = 0
                
        if r-i >= 0 and c+i<= 7 and dr:
            if gs.board[r-i][c+i] == "__":
                moves.append(Move((r,c), (r-i, c+i), gs.board))
            elif gs.board[r-i][c+i][0] == "b" and gs.whiteToMove or gs.board[r-i][c+i][0] == "w" and not gs.whiteToMove:
                moves.append(Move((r,c), (r-i, c+i), gs.board))
                dr = 0
            elif gs.board[r-i][c+i][0] == "b" and not gs.whiteToMove or gs.board[r-i][c+i][0] == "w" and gs.whiteToMove:
                dr = 0
                
        if r-i >= 0 and c-i>=0 and dl:
            if gs.board[r-i][c-i] == "__":
                moves.append(Move((r,c), (r-i, c-i), gs.board))
            elif gs.board[r-i][c-i][0] == "b" and gs.whiteToMove or gs.board[r-i][c-i][0] == "w" and not gs.whiteToMove:
                moves.append(Move((r,c), (r-i, c-i), gs.board))
                dl = 0
            elif gs.board[r-i][c-i][0] == "b" and not gs.whiteToMove or gs.board[r-i][c-i][0] == "w" and gs.whiteToMove:
                dl = 0

def getQueenMoves(gs, r, c, moves):              
    getRookMoves(gs, r, c, moves)
    getBishopMoves(gs, r, c, moves)

def getKingMoves(gs, r, c, moves):              
        rows = [0, 0, 1, -1, 1, 1, -1, -1]
        cols = [1, -1, 0, 0, 1, -1, 1, -1]
        
        for i, j in zip(rows, cols):
             if r+i >= 0 and r+i <= 7 and c+i <= 7 and c+i >= 0:
                if gs.board[r+i][c+j] == "__":
                    moves.append(Move((r,c), (r+i, c+j), gs.board))
                elif gs.board[r+i][c+j][0] == "b" and gs.whiteToMove or gs.board[r+i][c+j][0] == "w" and not gs.whiteToMove:
                    moves.append(Move((r,c), (r+i, c+j), gs.board))