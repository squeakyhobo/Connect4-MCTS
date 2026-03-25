from game import Connect4
import math
import numpy as np

class MCTSNode():

    def __init__(self,board,parent,EXPLORATION_CONSANT):
        self.visits =0
        self.wins =0
        self.board = board
        self.parent = parent 
        self.children ={}
        self.EXPLORATION_CONSANT =EXPLORATION_CONSANT
    
    def unexplored_moves(self):
        unexplored_moves =[]
        # combination of legal moves and ones not visted 
        legal_moves = self.board.get_valid_moves()
        for move in legal_moves:
            if not(move in self.children):
                unexplored_moves.append(move)
        
        return unexplored_moves
    
    def calculate_uct(self):
        exploitation = self.wins/self.wins

        exploration = math.sqrt(math.log(self.parent.visits)/self.visits)

        return(exploitation + (self.EXPLORATION_CONSANT*exploration))




class MCTSTree():

    def __init__(self):
        
        root = MCTSNode(Connect4(np.zeros((6, 7), dtype=int)),1)

    def selection(self):
        #make its so you keep going down the tree via higest UCT then at leaf node pick random unvisted move 
        cursor = self.root
        while(True):
            unexplored_moves = cursor.unexplored_moves()
            #means there are moves to explire and create new child node
            if(len(unexplored_moves)!=0):
                self.expansion(cursor)

            # proceed to next node via max uct 
            else:
                #expand move
                pass

        

    def expansion(self,parent):
        
        new_leaf_node = MCTSNode(board_state,parent,EXPLORATION_CONSANT)
        return new_leaf_node

    def simulation():
        pass

    def backprop():
        pass


