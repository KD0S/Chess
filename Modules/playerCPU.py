import pygame as p
from Modules import ChessEngine
from Modules.Move import Move
from Modules.utils import Utils, Clock
from Modules.checks import isCheck
from Modules.Ai import Ai

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
                                    gs.boardPieces[gs.player+'p']-=1
                                    gs.boardPieces[piece]+=1
                                print(move.getChessNotation())
                                moveMade = True
            
            else:
                move = bots.greedyBot(gs)
                if move !=  None:
                    gs.makeMove(move)
                    if move.pawnPromotion:
                            piece = gs.enemy+'Q'
                            gs.board[move.endRow][move.endCol] = piece
                            gs.boardPieces[gs.enemy+'p']-=1
                            gs.boardPieces[gs.enemy+'Q']+=1
                    print(move.getChessNotation())
                moveMade = True

            if moveMade:
                validMoves = gs.getValidMoves()
                turn, ally = utils.getTurnAlly(gs.playerToMove)
                (Kr, Kc) = gs.getKingLocation(ally)
                check = isCheck(gs.board, ally, player, Kr, Kc)

                if len(validMoves)==0:
                    boardNotation = gs.FEN.positionTOFEN(gs.board)
                    print(boardNotation)
                    if check:
                        running = utils.endScreen(turn, 'check')
                        break
                    if gs.inSuffiecientMaterial:
                        running = utils.endScreen('w', 'material')
                        break
                    elif gs.threeFoldRepition:
                        running = utils.endScreen('w', 'repetition')
                        break
                    else:
                        running = utils.endScreen('w', 'stalemate')
                moveMade = False

        utils.drawGameState(gs, currSq, validMoves, check)
if __name__ == '__main__':
    main(player)
