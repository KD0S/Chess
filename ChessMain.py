import pygame as p
import ChessEngine
from Move import Move
import time
from utils import Utils

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
    utils = Utils(p, DIMENSION, SQ_SIZE, IMAGES)
    p.display.set_icon(IMAGES['wN'])
    utils.display_rankFile(screen)
    running = True
    validMoves = gs.getValidMoves(gs)
    moveMade = False
    check = False
    clock.tick(MAX_FPS)
    utils.updateDisplay(screen, gs)
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
                utils.highlight_cells(screen, cells, gs.board, startSq, check, gs)

                
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
                        if move.pieceCaptured[1] == "K":
                            utils.win(screen, move)
                            time.sleep(3)
                            running = False
                            break
                        moveMade = True
                        utils.updateDisplay(screen, gs)
                
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    utils.updateDisplay(screen, gs)
            
            if moveMade:
                validMoves = gs.getValidMoves(gs)
                ally = "w" if gs.whiteToMove else "b"
                if gs.isCheck(ally):
                    check = True
                else:
                    check = False
                moveMade = False

if __name__ == '__main__':
    main()
  
    
    
