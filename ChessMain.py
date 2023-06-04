import pygame as p
import ChessEngine
from Move import Move

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
X_OFFSET = 100
y_OFFSET = 100


def loadImages():
    pieces = ['bN', 'bQ', 'bK',
              'bB', 'bR', 'bp',
              'wN', 'wQ', 'wK',
              'wB', 'wR', 'wp']
    
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("./images/"+piece+".png"), (SQ_SIZE, SQ_SIZE))
    

def main():
    
    p.init()
    screen = p.display.set_mode((800, 700))
    p.display.set_caption('Chess')
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    gs = ChessEngine.GameState()
    loadImages()
    p.display.set_icon(IMAGES['wN'])
    running = True
    validMoves = gs.getValidMoves(gs)
    moveMade = False
    clock.tick(MAX_FPS)
    updateDisplay(screen, gs)
    
    while running:
        for e in p.event.get():      
            
            if e.type == p.QUIT:
                running = False
                
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = (location[0]-50)//SQ_SIZE
                row = (location[1]-50)//SQ_SIZE
                if row > 7 or row < 0 or col > 7 or col < 0:
                    continue
                startSq = (row, col)
                cells = gs.displayPossibleMoves(row, col, validMoves) 
                highlight_cells(screen, cells, gs.board, startSq)
                
            elif e.type == p.MOUSEBUTTONUP:
                location = p.mouse.get_pos()
                col = (location[0]-50)//SQ_SIZE
                row = (location[1]-50)//SQ_SIZE
                if row > 7 or row < 0 or col > 7 or col < 0:
                    continue
                endSq = (row, col)
                if startSq != endSq:
                    move = ChessEngine.Move(startSq, endSq, gs.board)
                    if move in validMoves:
                        print(move.getChessNotation())
                        gs.makeMove(move)
                        moveMade = True
                        updateDisplay(screen, gs)
                
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    updateDisplay(screen, gs)
            
            if moveMade:
                validMoves = gs.getValidMoves(gs)
                moveMade = False

def highlight_cells(screen, cells, board, startSq):
    drawBoard(screen)
    for cell in cells:
        highlight(screen, 100, (0,255,0), cell[1], cell[0])
    highlight(screen, 100, (0,0,255), startSq[1], startSq[0])
    drawPieces(screen, board)
    p.display.update()


def highlight(screen, alpha, color, x, y):
    s = p.Surface((SQ_SIZE, SQ_SIZE))
    s.set_alpha(alpha)
    s.fill(color)
    screen.blit(s, (x*SQ_SIZE+50, y*SQ_SIZE+50))

 
def updateDisplay(screen, gs):
    drawGameState(screen, gs)
    p.display.update()


def drawBoard(screen):
    colors = [(238,238,210), (118,150,86)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE+50, r*SQ_SIZE+50, SQ_SIZE, SQ_SIZE))
            
            
def drawPieces(screen, board): 
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "__":
                screen.blit(IMAGES[piece],  p.Rect(c*SQ_SIZE+50, r*SQ_SIZE+50, SQ_SIZE, SQ_SIZE))


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def draw_text(screen, text, text_col, x, y):
    font = p.font.SysFont("Arial", 12)
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

if __name__ == '__main__':
    main()
  
    
    
