import random

class Ai():
    def __init__(self):
        self.KWt = 20
        self.QWt = 9
        self.RWt = 5
        self.BWt = 3
        self.NWt = 3
        self.pWt = 1
        
        self.weights = [self.KWt, self.QWt, self.RWt, self.BWt, self.NWt, self.pWt]
        self.mobilityWt = 2
  
    def ComplexEvalCPU(self, gs):     
        materialScore = 0
        mobilityScore = 0
        
        for piece, weight in zip(gs.pieces, self.weights):
            materialScore += (weight*(gs.boardPieces[gs.enemy+piece]-
                gs.boardPieces[gs.player+piece]))
        
        if gs.playerToMove:
            PlayerMobility = gs.getValidMoves()
            gs.playerToMove = not gs.playerToMove
            EnemyMobility = gs.getValidMoves()
        else:
            EnemyMobility = gs.getValidMoves()
            gs.playerToMove = not gs.playerToMove
            PlayerMobility = gs.getValidMoves()
        
        gs.playerToMove = not gs.playerToMove       
        
        mobilityScore = self.mobilityWt*(len(EnemyMobility) - len(PlayerMobility))
        
        Eval = materialScore + mobilityScore
        
        return Eval
    
    def SimpleEval(self, gs):
        materialScore = 0
        
        for piece, weight in zip(gs.pieces, self.weights):
            materialScore += (weight*(gs.boardPieces[gs.enemy+piece]-
                gs.boardPieces[gs.player+piece]))      
        
        return materialScore
    
    def search(self, depth, gs):
        
        if(depth == 0):
            return None, self.SimpleEval(gs)
        
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
        selectedMove = moves[random.randint(0, len(moves)-1)]
        for move in moves:
            gs.makeMove(move)
            currScore = self.ComplexEvalCPU(gs)
            gs.undoMove()
            if currScore > maxEvalScore:
                maxEvalScore = currScore
                selectedMove = move
        return selectedMove
        
    def minimaxBot(self, gs):
        move, _ = self.search(3, gs)
        return move