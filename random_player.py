import random
from player import Player

class RandomPlayer(Player):
    """ a subclass for an unintelligent computer player
    """
    def next_move(self, b):
        """ overrides the inherited next_move """
        self.num_moves += 1
        available_indices = [col for col in range(b.width) if b.can_add_to(col) == True]
        return random.choice(available_indices)