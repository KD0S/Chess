class Eval:
    def __init__(self):
        self.KWt = 0
        self.QWt = 90
        self.RWt = 50
        self.BWt = 30
        self.NWt = 30
        self.pWt = 10
        
        self.weights = [self.KWt, self.QWt, self.RWt, self.BWt, self.NWt, self.pWt]
        self.mobilityWt = 2
        
    def ComplexEvalCPU(self, gs):    
        materialScore = 0
        mobilityScore = 0
        
        materialScore = self.getMaterialScore(gs)
        
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
    
    def checkIsolatedPawns(self, player):
        pass
    
    def getMaterialScore(self, gs):
        materialScore = 0
        
        for piece, weight in zip(gs.pieces, self.weights):
            materialScore += (weight*(gs.boardPieces[gs.enemy+piece]-
                gs.boardPieces[gs.player+piece]))      
        
        return materialScore