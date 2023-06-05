from Move import Move
import colors

class Utils():
    
    def __init__(self, p, DIMENSION, SQ_SIZE, IMAGES):
        self.p = p
        self.DIMENSION = DIMENSION
        self.SQ_SIZE = SQ_SIZE
        self.IMAGES = IMAGES
    
    def drawBoard(self, screen):
        clrs = [colors.darkGreen, colors.lightGreen]
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                clr = clrs[((r+c)%2)]
                self.p.draw.rect(screen, clr, self.p.Rect(c*self.SQ_SIZE+50, r*self.SQ_SIZE+50, self.SQ_SIZE, self.SQ_SIZE))
                   
    def drawPieces(self, screen, board): 
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                piece = board[r][c]
                if piece != "__":
                    screen.blit(self.IMAGES[piece],  self.p.Rect(c*self.SQ_SIZE+50, r*self.SQ_SIZE+50, self.SQ_SIZE, self.SQ_SIZE))
    
    def drawGameState(self, screen, gs, currSq, validMoves, check):
        self.drawBoard(screen)
        if currSq != ():
            cells = gs.displayPossibleMoves(currSq[0], currSq[1], validMoves) 
            self.highlight_cells(screen, cells, gs.board, currSq, check, gs)
        self.drawPieces(screen, gs.board)
        self.p.display.update()    
    
    def display_rankFile(self, screen, player):
        font = self.p.font.SysFont(None, 26)
        clrs = [colors.darkGreen, colors.lightGreen]
        for i in range(8):
            clr = clrs[i%2]
            img = font.render(Move.rowToRanks[i], True, clr)
            screen.blit(img, (20, i*64+60))
        for i in range(8):
            clr = clrs[(i+7)%2]
            img = font.render(Move.colsToFiles[i], True, clr)
            screen.blit(img, (i*64+70, 580))
    
    def highlight(self, screen, alpha, color, x, y):
        s = self.p.Surface((self.SQ_SIZE, self.SQ_SIZE))
        s.set_alpha(alpha)
        s.fill(color)
        screen.blit(s, (x*self.SQ_SIZE+50, y*self.SQ_SIZE+50))
            
    def highlight_cells(self, screen, cells, board, startSq, check, gs):
        self.drawBoard(screen)
        for cell in cells:
            self.highlight(screen, 100, colors.green, cell[1], cell[0])
        self.highlight(screen, 100, colors.blue, startSq[1], startSq[0])
        if check == True:
            self.highlight_check(screen, gs)

    def highlight_check(self, screen, gs):
        ally = "w" if gs.whiteToMove else "b"
        if ally == "w":
            Kr, Kc = gs.whiteKingLocation
        else:
            Kr, Kc = gs.blackKingLocation
        self.highlight(screen, 150, (255, 0, 0), Kc, Kr)

    def win(self, screen, move, check):
        if check:
            if move.pieceCaptured[0] == "w":
                text = "Black Wins!"
            else:
                text = "White Wins!"
        else:
            text = "StaleMate!"
        
        textColor = (238,238,210)
        bgColor = (118,150,86) 
        screen.fill(bgColor)
        font = self.p.font.SysFont(None, 60)
        img = font.render(text, True, textColor)
        screen.blit(img, (256 , 200))
        self.p.display.update()
    
    def GetMouseXY(self):
        location = self.p.mouse.get_pos()
        col = (location[0]-50)//self.SQ_SIZE
        row = (location[1]-50)//self.SQ_SIZE
        if row > 7 or row < 0 or col > 7 or col < 0:
            row, col = -1, -1
            return row, col
        else:
            return row, col
        