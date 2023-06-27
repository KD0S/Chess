from ChessEngine import GameState

gs = GameState('w')

def moveGenerationTest(depth):
    if depth == 0:
        return 1
    numPositions = 0
    moves = gs.getValidMoves()
    for move in moves:
        gs.makeMove(move)
        numPositions += moveGenerationTest(depth-1)
        gs.undoMove()
    return numPositions

print(moveGenerationTest(4))