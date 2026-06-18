"""
Tic Tac Toe Player
"""

from copy import deepcopy

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
        # calculate the amount of moves have been played
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
        action_set = set()
        # iterate through the board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == EMPTY:
                    action_set.add((i, j))
        return action_set
    else:
        return set()


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    available_actions = actions(board)
    if action not in available_actions:
        raise RuntimeError("Not a valid action")
    current_player = player(board)
    i, j = action
    new_board = deepcopy(board)
    new_board[i][j] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # get the transposed board
    transposed_board = transpose_board(board)
    # check the rows
    row_val = check_rows(board)
    if row_val: return row_val
    # check the columns 
    col_val = check_rows(transposed_board)
    if col_val: return col_val
    # Check the diagonals 
    diag_val = check_diagonals(board)
    if diag_val: return diag_val
    # check the transverse diagonal
    tra_diag_val = check_diagonals(transposed_board)
    if tra_diag_val: return tra_diag_val
    return EMPTY




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check the winner
    if winner(board): return True
    # Check filled board
    else: 
        for row in board:
            for cell in row:
                if cell == EMPTY: return False
                else: pass
        return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    Winner = winner(board)
    if Winner == X: return 1
    elif Winner == O: return -1
    else: return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # return None if the board is in terminal state
    is_maximizing = True if player(board) == X else False

    if terminal(board): return None

    current_player = player(board)

    if current_player == X:
        #Maximizer: try to maximize the score
        best_score = float("-inf")
        best_action = None
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
        return best_action

    else:
        # Minimizer
        best_score = float("inf")
        best_action = None
        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action
        return best_action



def check_rows(board):
    # check the rows
    for row in board:
        set_row = set(row)
        if len(set_row) == 1:
            if set_row == {EMPTY}: pass
            else: return next(iter(set_row))
    return EMPTY


def transpose_board(board):
    new_board = []
    # loop though column indices (0, 1, 2)
    for i in range(len(board[0])):
        new_row = []
        # loop through each row to grab the item at index i
        for row in board:
            new_row.append(row[i])
        new_board.append(new_row)
    return new_board


def check_diagonals(board):
    # main diagonal
    main_diag = {board[i][i] for i in range(len(board))}
    if len(main_diag) == 1 and EMPTY not in main_diag:
        return next(iter(main_diag))

    # anti-diagonal
    anti_diag = {board[i][len(board) - 1 - i] for i in range(len(board))}
    if len(anti_diag) == 1 and EMPTY not in anti_diag:
        return next(iter(anti_diag))

    return EMPTY


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v