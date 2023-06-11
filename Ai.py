import random

class Ai():

    def randomBot(moves):
        i = random.randint(0, len(moves)-1)
        return moves[i]