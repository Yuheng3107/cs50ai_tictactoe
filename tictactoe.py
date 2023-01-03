"""
Tic Tac Toe Player
"""

from cmath import inf
import math
from re import M
import copy

X = "X"
O = "O"
EMPTY = None
d = {}

class NotValidAction(Exception):
    def __init__(self, message="Action is not valid"):
        self.message = message
        super().__init__(self.message)
        

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty_spaces = 0
    for row in board:
        for cell in row:
            if cell is None:
                empty_spaces += 1
    if (empty_spaces % 2 == 1):
        return "X"
    else:
        return "O"

            



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is None:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    new_board = copy.deepcopy(board)
    i, j = action
    if board[i][j] is not None:
        raise NotValidAction
    

    new_board[i][j] = player(new_board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True
                



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Board is getting modified all the way at once
    if terminal(board):
        return None
    
    if player(board) == X:
        action, util = maxValue(board)
    else:
        action, util = minValue(board)
    
    return action
    
def maxValue(board):
    # Returns tuple of maxValue achieved, and optimal action
    if (terminal(board)):
        return (None, utility(board))
    v = -inf
    
    for action in actions(board):
        _, minval = minValue(result(board, action))
        if minval > v:
            v = minval
            maxAction = action
    return (maxAction, v)


def minValue(board):
    # returns tuple of minValue achieved, and optimal action
    if (terminal(board)):
        return (None, utility(board))
    
    v = inf
    for action in actions(board):
        _, maxval = maxValue((result(board, action)))
        if maxval < v:
            v = maxval
            minAction = action
    return (minAction, v)


