import pygame as p
import ChessEngine
from Move import Move
from utils import Utils
from utils import Clock
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
        image = p.image.load("./Assets/images/"+piece+".png").convert_alpha()       
        image = p.transform.scale(image, (SQ_SIZE, SQ_SIZE))
        IMAGES[piece] = image


def main(player, timed):
    p.init()
    screen = p.display.set_mode((700, 600))
    p.display.set_caption('Chess')
    screen.fill((18, 18, 18))
    gs = ChessEngine.GameState(player)
    loadImages()
    utils = Utils(p, DIMENSION, SQ_SIZE, IMAGES, player, screen)
    p.display.set_icon(IMAGES['wN'])
    utils.display_rankFile(player)
    running = True
    validMoves = gs.getValidMoves()
    moveMade = False
    check = False
    selectedCells = []
    currSq = ()
    utils.drawGameState(gs, currSq, validMoves, check)
    player2Clock =  Clock(p, screen, 8.3, 0)
    player1Clock =  Clock(p, screen, 8.3, 7.5)
    if timed:
        player1Time = 300
        player2Time = 300
    else:
        player1Time = None
        player2Time = None   
    player1Clock.draw(player1Time)
    player2Clock.draw(player2Time)
    if time:
        clock = p.time.Clock()
        startTime = time.time()
    while running:
        clock.tick(30)
        if gs.playerToMove and timed:
            player1Time -= time.time() - startTime
            if player1Time <= 0:
                running = utils.endScreen(gs.enemy, 'time')
                break
            player1Clock.draw(player1Time)
            
        elif not gs.playerToMove and timed:
            player2Time -= time.time() - startTime
            if player2Time <= 0:
                running = utils.endScreen(gs.player, 'time')
                break
            player2Clock.draw(player2Time)
            
        if timed:
            startTime = time.time()
        
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
                    currMove = Move(selectedCells[0], selectedCells[1], gs.board)
                    selectedCells = []
                    currSq = ()
                    for move in validMoves:
                        if move == currMove:
                            gs.makeMove(move)
                            if move.pawnPromotion:
                                    if not gs.playerToMove:
                                        color = gs.player
                                    else:
                                        color = gs.enemy
                                    piece = utils.pawnPromotionMenu(move.endRow, move.endCol, color, IMAGES)
                                    gs.board[move.endRow][move.endCol] = piece
                            print(move.getChessNotation())
                            moveMade = True

            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    selectedCells = []
                    currSq = ()

            if moveMade:
                
                validMoves = gs.getValidMoves()
                       
                if len(validMoves)==0:
                    if gs.inSuffiecientMaterial:
                        running = utils.endScreen('w', 'material')
                        break
                    elif gs.threeFoldRepition:
                        running = utils.endScreen('w', 'repetition')
                        break
                    else:
                        running = utils.endScreen('w', 'stalemate')
                        break
                        
                
                # is opponent in check?
                gs.playerToMove = not gs.playerToMove
                turn, ally = utils.getTurnAlly(gs.playerToMove)
                (Kr, Kc) = gs.getKingLocation(ally)
                check = isCheck(gs.board, ally, player, Kr, Kc)
                if check:
                    running = utils.endScreen(turn, 'check')
                    break

                # is player in check?
                gs.playerToMove = not gs.playerToMove
                turn, ally = utils.getTurnAlly(gs.playerToMove)
                (Kr, Kc) = gs.getKingLocation(ally)
                check = isCheck(gs.board, ally, player, Kr, Kc)
                if len(validMoves) == 0:
                    running = utils.endScreen(turn, 'check')
                    break
                moveMade = False

        utils.drawGameState(gs, currSq, validMoves, check)

if __name__ == '__main__':
    main()




