import pygame as p
import ChessEngine
from Move import Move
from utils import Utils, Clock
from checks import isCheck
from Ai import Ai

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

player = "w"

def main(player):
    p.init()
    screen = p.display.set_mode((700, 600))
    p.display.set_caption('Chess')
    screen.fill((18, 18, 18))
    
    gs = ChessEngine.GameState(player)
    loadImages()
    utils = Utils(p, DIMENSION, SQ_SIZE, IMAGES, player, screen)
    p.display.set_icon(IMAGES['wN'])
    utils.display_rankFile(player)    
    # player2Clock =  Clock(p, screen, 8.3, 0)
    # player1Clock =  Clock(p, screen, 8.3, 7.5)
    # # player1Time = gs.player
    # # player2Time = gs.enemy
    # # player1Clock.draw(player1Time)
    # # player2Clock.draw(player2Time)
    
    running = True
    validMoves = gs.getValidMoves()
    moveMade = False
    check = False
    selectedCells = []
    currSq = ()
    utils.drawGameState(gs, currSq, validMoves, check)
    bots = Ai()
    clock = p.time.Clock()
    
    while running:
        clock.tick(30)        
        for e in p.event.get():

            if e.type == p.QUIT:
                running = False
            
            if e.type == p.KEYDOWN and e.key == p.K_z:
                gs.undoMove()
                moveMade = True
                selectedCells = []
                currSq = ()

            if gs.playerToMove:
                if e.type == p.MOUSEBUTTONDOWN:
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
                                    piece = utils.pawnPromotionMenu(move.endRow, move.endCol, gs.player, IMAGES)
                                    gs.board[move.endRow][move.endCol] = piece
                                print(move.getChessNotation())
                                moveMade = True
            
            else:
                if len(validMoves) == 0:
                    if gs.inSuffiecientMaterial:
                        running = utils.endScreen(gs.enemy, 'material')
                        break
                    check = isCheck(gs.board, gs.enemy, player, 
                                    gs.enemyKingLocation[0], gs.enemyKingLocation[1])
                    running = utils.endScreen(gs.enemy, 'check')
                    break
                move = bots.greedyBot(gs)
                gs.makeMove(move)
                if move.pawnPromotion:
                        # # random bot
                        # piece = Ai.randomBot([gs.enemy+'R', gs.enemy+'N', gs.enemy+'B', gs.enemy+'Q'], gs)
                        piece = gs.enemy+'Q'
                        gs.board[move.endRow][move.endCol] = piece
                print(move.getChessNotation())
                moveMade = True

            if moveMade:
                validMoves = gs.getValidMoves()
                
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
    main(player)
