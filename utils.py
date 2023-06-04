from Move import Move

class Utils():
    def __init__(self, p, DIMENSION, SQ_SIZE, IMAGES):
        self.p = p
        self.DIMENSION = DIMENSION
        self.SQ_SIZE = SQ_SIZE
        self.IMAGES = IMAGES

    def highlight_cells(self, screen, cells, board, startSq, check, gs):
        self.drawBoard(screen)
        for cell in cells:
            self.highlight(screen, 100, (0,255,0), cell[1], cell[0])
        self.highlight(screen, 100, (0,0,255), startSq[1], startSq[0])
        if check == True:
            self.highlight_check(screen, gs)
        self.drawPieces(screen, board)
        self.p.display.update()

    def display_rankFile(self, screen):
        font = self.p.font.SysFont(None, 24)
        for i in range(8):
            img = font.render(Move.rowToRanks[i], True, (255, 255, 255))
            screen.blit(img, (20, i*64+60))
        for i in range(8):
            img = font.render(Move.colsToFiles[i], True, (255, 255, 255))
            screen.blit(img, (i*64+70, 580))
        
    def highlight(self, screen, alpha, color, x, y):
        s = self.p.Surface((self.SQ_SIZE, self.SQ_SIZE))
        s.set_alpha(alpha)
        s.fill(color)
        screen.blit(s, (x*self.SQ_SIZE+50, y*self.SQ_SIZE+50))

    
    def updateDisplay(self, screen, gs):
        self.drawGameState(screen, gs)
        self.p.display.update()

    def win(self, screen, move):
        if move.pieceCaptured[0] == "w":
            text = "Black Wins!"
            textColor = (0, 0, 0)
            bgColor = (255, 255, 255)
        else:
            text = "White Wins!"
            textColor = (255, 255, 255)
            bgColor = (0, 0, 0)
        screen.fill(bgColor)
        font = self.p.font.SysFont("Arial", 60)
        img = font.render(text, True, textColor)
        screen.blit(img, (256 , 200))
        self.p.display.update()


    def drawBoard(self, screen):
        colors = [(238,238,210), (118,150,86)]
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                color = colors[((r+c)%2)]
                self.p.draw.rect(screen, color, self.p.Rect(c*self.SQ_SIZE+50, r*self.SQ_SIZE+50, self.SQ_SIZE, self.SQ_SIZE))
                
                
    def drawPieces(self, screen, board): 
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                piece = board[r][c]
                if piece != "__":
                    screen.blit(self.IMAGES[piece],  self.p.Rect(c*self.SQ_SIZE+50, r*self.SQ_SIZE+50, self.SQ_SIZE, self.SQ_SIZE))

    def highlight_check(self, screen, gs):
        ally = "w" if gs.whiteToMove else "b"
        if ally == "w":
            Kr, Kc = gs.whiteKingLocation
        else:
            Kr, Kc = gs.blackKingLocation
        self.highlight(screen, 150, (255, 0, 0), Kc, Kr)

    def drawGameState(self, screen, gs):
        self.drawBoard(screen)
        self.drawPieces(screen, gs.board)