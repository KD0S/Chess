import random
from Modules.eval import Eval

class Ai():
    
    def __init__(self):
        self.CHECKMATE = "check"
        self.eval = Eval()
    
    def search(self, depth, gs):
        if(depth == 0):
            return None, self.eval.getMaterialScore(gs)
        
        moves = gs.getValidMoves()
        maxEval = -10000
        
        if(len(moves) == 0):
            return None, -100000
        
        for move in moves:
            gs.makeMove(move)
            if gs.playerToMove:
                _, utility = self.search(depth-1, gs)
                utility = -utility
            else:
                _, utility = self.search(depth-1, gs)
            gs.undoMove()
            if utility > maxEval:
                maxEval = utility
                selectedMove = move
                
        return selectedMove, maxEval
    
    def randomBot(self, gs):
        moves = gs.getValidMoves()
        i = random.randint(0, len(moves)-1)
        return moves[i]

    def greedyBot(self, gs):
        maxEvalScore = -300
        moves = gs.getValidMoves()
        if len(moves) == 0:
            return None
        selectedMove = moves[random.randint(0, len(moves)-1)]
        for move in moves:
            gs.makeMove(move)
            currScore = self.eval.ComplexEvalCPU(gs)
            gs.undoMove()
            if currScore > maxEvalScore:
                maxEvalScore = currScore
                selectedMove = move
        return selectedMove
        
    def minimaxBot(self, gs):
        move, _ = self.search(3, gs)
        return move