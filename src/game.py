import numpy as np
from typing import List, Tuple, Optional
 

class Connect4:
    def __init__(self, board_state=None, current_player=1):
        self.rows = 6
        self.cols = 7
        if board_state is None:
            self.board = np.zeros((self.rows, self.cols), dtype=int)
        else:
            self.board = board_state
        self.current_player = current_player
        self.last_move = None

    def get_valid_moves(self) -> List[int]:
        """Returns a list of columns that are not full."""
        return [c for c in range(self.cols) if self.board[0][c] == 0]

    def make_move(self, col: int) -> bool:
        """Drops a piece into the specified column. Returns False if move is invalid."""
        if self.board[0][col] != 0:
            return False
        
        for r in reversed(range(self.rows)):
            if self.board[r][col] == 0:
                self.board[r][col] = self.current_player
                self.last_move = (r, col)
                self.current_player *= -1 # Switch players
                return True
        return False

    def check_winner(self) -> Optional[int]:
        """
        Checks if the last move resulted in a win.
        Returns: 1 or -1 if there is a winner, 0 for a draw, None if ongoing.
        """
        if self.last_move is None:
            return None

        r, c = self.last_move
        player = self.board[r][c]

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            # Check forward and backward in the direction
            for delta in [1, -1]:
                nr, nc = r + dr * delta, c + dc * delta
                while 0 <= nr < self.rows and 0 <= nc < self.cols and self.board[nr][nc] == player:
                    count += 1
                    nr += dr * delta
                    nc += dc * delta
            if count >= 4:
                return player

        if len(self.get_valid_moves()) == 0:
            return 0  # Draw
        
        return None # Ongoing

    def copy(self):
        """Creates a deep copy of the game state for MCTS simulations."""
        new_game = Connect4(np.copy(self.board), self.current_player)
        new_game.last_move = self.last_move
        return new_game

    def __str__(self):
        """String representation for debugging and playing."""
        return str(self.board).replace('0', '.').replace('1', 'X').replace('-1', 'O')