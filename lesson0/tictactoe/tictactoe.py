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
    # fmt: off
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    # fmt: on


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    # check how many "X" and "O" are on the board
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    # if there is an even number of "X" and "O" on the board, it's "X"'s turn
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_coordinates = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_coordinates.add((i, j))

    return possible_coordinates


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    updated_board = board

    # check if the action is valid
    if action not in actions(board):
        raise Exception("Invalid action")

    # update the board
    updated_board[action[0]][action[1]] = player(board)

    return updated_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check if there is a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != EMPTY:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != EMPTY:
            return board[0][2]

        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check if there is a winner
    if winner(board) is not None:
        return True

    # check if there are any empty cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # check if there is a winner
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # check if the game is over
    if terminal(board):
        return None

    if player(board) == X:
        return max_value(board)

    return min_value(board)
