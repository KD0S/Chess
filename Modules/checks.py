def isCheck(board, ally, player, Kr, Kc):    
    # Check for Pawn
    if ally != player:
        if Kr+1 <= 7 and Kc+1 <= 7 and board[Kr+1][Kc+1][0] != ally:
            if board[Kr+1][Kc+1][1] == 'p':
                return True
        
        if Kr+1 <= 7 and Kc-1 >= 0 and board[Kr+1][Kc-1][0] != ally:
            if board[Kr+1][Kc-1][1] == 'p':
                return True
    else:
        if Kr-1 >= 0 and Kc+1 <= 7 and board[Kr-1][Kc+1][0] != ally:
            if board[Kr-1][Kc+1][1] == 'p':
                return True
        
        if Kr-1 >= 0 and Kc-1 >= 0 and board[Kr-1][Kc-1][0] != ally:
            if board[Kr-1][Kc-1][1] == 'p':
                return True
    
    # Check for Knight
    if Kr+2 <= 7 and Kc+1 <= 7 and board[Kr+2][Kc+1][0] != ally:
        if board[Kr+2][Kc+1][1] == 'N':
            return True
    
    if Kr+2 <= 7 and Kc-1 >= 0 and board[Kr+2][Kc-1][0] != ally:
        if board[Kr+2][Kc-1][1] == 'N':
            return True
    
    if Kr+1 <= 7 and Kc+2 <= 7 and board[Kr+1][Kc+2][0] != ally:
        if board[Kr+1][Kc+2][1] == 'N':
            return True
    
    if Kr+1 <= 7 and Kc-2 >= 0 and board[Kr+1][Kc-2][0] != ally:
        if board[Kr+1][Kc-2][1] == 'N':
            return True
    
    if Kr-2 >= 0 and Kc+1 <= 7 and board[Kr-2][Kc+1][0] != ally:
        if board[Kr-2][Kc+1][1] == 'N':
            return True
    
    if Kr-2 >= 0 and Kc-1 >= 0 and board[Kr-2][Kc-1][0] != ally:
        if board[Kr-2][Kc-1][1] == 'N':
            return True
    
    if Kr-1 >= 0 and Kc+2 <= 7 and board[Kr-1][Kc+2][0] != ally:
        if board[Kr-1][Kc+2][1] == 'N':
            return True
    
    if Kr-1 >= 0 and Kc-2 >= 0 and board[Kr-1][Kc-2][0] != ally:
        if board[Kr-1][Kc-2][1] == 'N':
            return True
    
    # Check for King
    rows = [0, 0, 1, -1, 1, 1, -1, -1]
    cols = [1, -1, 0, 0, 1, -1, 1, -1]
    
    for i, j in zip(rows, cols):
        if Kr+i >= 0 and Kc+j >= 0 and Kr+i <= 7 and Kc+j <= 7:
            if board[Kr+i][Kc+j][0] != ally and board[Kr+i][Kc+j][1] == 'K':
                return True
    
    # Check for Rook, Queen
    for i in range(1, 7, 1):
        if Kr+i <= 7:
            if board[Kr+i][Kc][0] == ally:
                break
            elif board[Kr+i][Kc][1] == 'R' or board[Kr+i][Kc][1] == 'Q':
                return True
            elif board[Kr+i][Kc][0] != '_' and board[Kr+i][Kc][1] != 'R' and board[Kr+i][Kc][1] != 'Q':
                break
    
    for i in range(1, 7, 1):
        if Kr-i >= 0:
            if board[Kr-i][Kc][0] == ally:
                break
            elif board[Kr-i][Kc][1] == 'R' or board[Kr-i][Kc][1] == 'Q':
                return True
            elif board[Kr-i][Kc][0] != '_' and board[Kr-i][Kc][1] != 'R' and board[Kr-i][Kc][1] != 'Q':
                break
    
    for i in range(1, 7, 1):
        if Kc+i <= 7:
            if board[Kr][Kc+i][0] == ally:
                break
            elif board[Kr][Kc+i][1] == 'R' or board[Kr][Kc+i][1] == 'Q':
                return True
            elif board[Kr][Kc+i][0] != '_' and board[Kr][Kc+i][1] != 'R' and board[Kr][Kc+i][1] != 'Q':
                break
    
    for i in range(1, 7, 1):
        if Kc-i >= 0:
            if board[Kr][Kc-i][0] == ally:
                break
            elif board[Kr][Kc-i][1] == 'R' or board[Kr][Kc-i][1] == 'Q':
                return True
            elif board[Kr][Kc-i][0] != '_' and board[Kr][Kc-i][1] != 'R' and board[Kr][Kc-i][1] != 'Q':
                break
    
    # Check for Bishop, Queen
    for i in range(1, 7, 1):
        if Kr+i <= 7 and Kc+i <= 7:
            if board[Kr+i][Kc+i][0] == ally:
                break
            elif board[Kr+i][Kc+i][1] == 'B' or board[Kr+i][Kc+i][1] == 'Q':
                return True
            elif board[Kr+i][Kc+i][0] != '_' and board[Kr+i][Kc+i][1] != 'B' and board[Kr+i][Kc+i][1] != 'Q':
                break
    
    for i in range(1, 7, 1):
        if Kr-i >= 0 and Kc+i <= 7:
            if board[Kr-i][Kc+i][0] == ally:
                break
            elif board[Kr-i][Kc+i][1] == 'B' or board[Kr-i][Kc+i][1] == 'Q':
                return True
            elif board[Kr-i][Kc+i][0] != '_' and board[Kr-i][Kc+i][1] != 'B' and board[Kr-i][Kc+i][1] != 'Q':
                break
    
    for i in range(1, 7, 1):
        if Kc-i >= 0 and Kr+i <= 7:
            if board[Kr+i][Kc-i][0] == ally:
                break
            elif board[Kr+i][Kc-i][1] == 'B' or board[Kr+i][Kc-i][1] == 'Q':
                return True
            elif board[Kr+i][Kc-i][0] != '_' and board[Kr+i][Kc-i][1] != 'B' and board[Kr+i][Kc-i][1] != 'Q':
                break
    
    for i in range(1, 7, 1):
        if Kc-i >= 0 and Kr-i >= 0:
            if board[Kr-i][Kc-i][0] == ally:
                break
            elif board[Kr-i][Kc-i][1] == 'B' or board[Kr-i][Kc-i][1] == 'Q':
                return True
            elif board[Kr-i][Kc-i][0] != '_' and board[Kr-i][Kc-i][1] != 'B' and board[Kr-i][Kc-i][1] != 'Q':
                break
    
            

             