import pygame as p
import ChessEngine
from Move import Move
from utils import Utils
from checks import isCheck
import time

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
    utils = Utils(p, DIMENSION, SQ_SIZE, IMAGES, player, screen)
    p.display.set_icon(IMAGES['wN'])
    utils.display_rankFile(player)
    running = True
    validMoves = gs.getValidMoves(gs)
    moveMade = False
    check = False
    selectedCells = []
    currSq = ()
    clock.tick(MAX_FPS)
    utils.drawGameState(gs, currSq, validMoves, check)
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
                        gs.makeMove(move)
                        print(move.getChessNotation())  
                        moveMade = True
                
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    selectedCells = []
                    currSq = ()
            
            if moveMade:
                validMoves = gs.getValidMoves(gs)
                # is opponent in check?
                gs.playerToMove = not gs.playerToMove
                turn, ally = utils.getTurnAlly(gs.playerToMove)
                (Kr, Kc) = gs.getKingLocation(ally)
                check = isCheck(gs, ally, player, Kr, Kc)
                if check:
                    utils.win(turn, check)
                    time.sleep(3)
                    running = False
                    break
                
                # is player in check?
                gs.playerToMove = not gs.playerToMove
                turn, ally = utils.getTurnAlly(gs.playerToMove)
                (Kr, Kc) = gs.getKingLocation(ally)
                check = isCheck(gs, ally, player, Kr, Kc)
                if len(validMoves) == 0:
                    utils.win(turn, check)
                    time.sleep(3)
                    running = False
                    break
                moveMade = False
                
        utils.drawGameState(gs, currSq, validMoves, check)
if __name__ == '__main__':
    main()
  
    
