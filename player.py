#
# A Connect-Four Player class 
#  

class Player:
    """ a data type for a Connect Four player
    """ 
    def __init__(self, checker):
        """ initializes attributes """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string that represents a Player object
        """
        return 'Player ' + self.checker
    
    def opponent_checker(self):
        """ returns a string that represents the 
            checker of the Player object's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ get a next move for this player
            that is valid for the board b
        """
        self.num_moves += 1
        
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')