import pygame as p
import ChessEngine
from Move import Move
import time
from utils import Utils
from checks import isCheck

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ['bN', 'bQ', 'bK',
              'bB', 'bR', 'bp',
              'wN', 'wQ', 'wK',
              'wB', 'wR', 'wp']
    
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("./images/"+piece+".png"), (SQ_SIZE, SQ_SIZE))
    

def main(player):
    p.init()
    screen = p.display.set_mode((800, 700))
    p.display.set_caption('Chess')
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    gs = ChessEngine.GameState(player)
    loadImages()
    utils = Utils(p, DIMENSION, SQ_SIZE, IMAGES)
    p.display.set_icon(IMAGES['wN'])
    utils.display_rankFile(screen, player)
    running = True
    validMoves = gs.getValidMoves(gs)
    moveMade = False
    check = False
    selectedCells = []
    currSq = ()
    clock.tick(MAX_FPS)
    utils.drawGameState(screen, gs, currSq, validMoves, check)
    while running:
        for e in p.event.get():      
            
            if e.type == p.QUIT:
                running = False
                
            elif e.type == p.MOUSEBUTTONDOWN:
                row, col = utils.GetMouseXY()
                if row==-1 and col==-1:
                    continue
                
                if (row, col) == currSq:
                    currSq = ()
                    selectedCells = []
                else:
                    currSq = (row, col)
                    selectedCells.append(currSq)
                        
                if len(selectedCells)==2:
                    move = Move(selectedCells[0], selectedCells[1], gs.board)
                    selectedCells = []
                    currSq = ()
                    if move in validMoves:
                        print(move.getChessNotation())
                        gs.makeMove(move)
                        moveMade = True
                
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    selectedCells = []
                    currSq = ()
            
            if moveMade:
                validMoves = gs.getValidMoves(gs)
                ally = "w" if gs.whiteToMove else "b"
                if isCheck(gs, ally):
                    check = True
                else:
                    check = False
                if len(validMoves) == 0:
                    utils.win(screen, move, check)
                    time.sleep(3)
                    running = False
                    break
                moveMade = False
                
        utils.drawGameState(screen, gs, currSq, validMoves, check)
if __name__ == '__main__':
    main()
  
    
