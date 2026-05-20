"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


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
    if not terminal(board):
        moved = 0
        # calculate the ammount of moves've been played
        for row in board:
            for cell in row:
                if cell != EMPTY:
                    moved += 1
        # determine the move through even and odd number of moves
        if moved & 1:
            return O 
        else: 
            return X 
    else:
        return EMPTY


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if not terminal(board):
        actions = set()
        # iterate through the board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == EMPTY:
                    actions.add((i, j))
        return actions
    else:
        return EMPTY


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
