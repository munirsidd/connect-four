#
# AI Player for use in Connect Four  
#

import random  
from player import Player

class AIPlayer(Player):
    """ a subclass for an intelligent computer player
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ initializes attributes """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self. lookahead = lookahead
        
    def __repr__(self):
        """ returns a string that represents an AIPlayer object
        """
        return 'Player ' + self.checker + ' ('+ self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """ returns the index of the column in scores
            with the maximum score
        """
        max_score = max(scores)
        max_list = []
        
        for col in range(len(scores)):
            if scores[col] == max_score:
                max_list += [col]
                
        if self.tiebreak == 'LEFT':
            return max_list[0]
        elif self.tiebreak == 'RIGHT':
            return max_list[-1]
        else:
            return random.choice(max_list)
            
    def scores_for(self, b):
        """ returns a list containing one score for each column
            in b for the called AIPlayer self
        """
        scores = [50] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(super().opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opp = AIPlayer(super().opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opp.scores_for(b)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                else:
                    scores[col] = 50
                b.remove_checker(col)
                
        return scores
    
    def next_move(self, b):
        """ overrides the inherited next_move """
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))