"""
Tic Tac Toe Player
"""
import copy
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

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_action=set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possible_action.add((i,j))
    
    return possible_action

def player(board):
    """
    Returns player who has the next turn on a board.
    """

    countX = 0
    countY = 0

    for i in range(3):
        for j in range(3):
            if board[i][j]=='X':
                countX+=1
            elif board[i][j]=='O':
                countY+=1
    
    if countX==countY:
        return X
    else:
        return O

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action[0] >= 3 or action[0] < 0 or action[1] >= 3 or action[1] < 0:
        raise Exception("INVALID INPUT")
    
    if board[action[0]][action[1]] is not None:
        raise Exception("INVALID INPUT")

    new_board=copy.deepcopy(board)

    new_board[action[0]][action[1]]=player(board)

    return new_board


def winner(board):

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] and board[0][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == 'X' or winner(board) == 'O':
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_val = -math.inf
        best_move = None
        for action in actions(board):
            move_val = min_value(result(board, action))
            if move_val > best_val:
                best_val = move_val
                best_move = action
        return best_move

    elif current_player == O:
        best_val = math.inf
        best_move = None
        for action in actions(board):
            move_val = max_value(result(board, action))
            if move_val < best_val:
                best_val = move_val
                best_move = action
        return best_move

#checking opponent best move
def max_value(board):

    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):

    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
