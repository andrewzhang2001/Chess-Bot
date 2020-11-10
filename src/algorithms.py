#IMPORT STATEMENTS
import chess


WHITEWIN = 10000
BLACKWIN = -10000
DRAW = 0

def naive_alphabeta(board, N, board_eval_func):
    """
    A general alpha-beta algorithm that searches N moves deep (white and black moves distinct).
    Used as a temlate for more advanced Alpha-Beta algorithms.
    Parameters
    ----------
    board: a board object from the chess-python library
    N: the number of moves remaining
    Return value
    ------------
    python-chess Move object: the best move for the current player
    """
    board_score = board_eval_func
    nodes_expanded = 0

    def alphabeta(board, depth, maximizing_player, alpha=float("-inf"), beta=float("inf")):
        nonlocal nodes_expanded
        nodes_expanded+=1
        if board.is_game_over():
            result = board.result()
            if result == "1-0":
                return WHITEWIN, None
            if result == "0-1":
                return BLACKWIN, None
            if result == "1/2-1/2":
                return DRAW, None
            else:
                raise ValueError("Result must be one of the above options")
        elif depth == 0:
            return board_score(), None

        else:
            if maximizing_player:
                bestScore = float("-inf")
                bestMove = None
                for move in board.legal_moves:
                    board.push(move)
                    move_value, _ = alphabeta(board, depth - 1, False, alpha, beta)
                    board.pop()
                    if move_value > bestScore:
                        bestScore = move_value
                        bestMove = move
                    alpha = max(alpha, move_value)
                    if alpha >= beta:
                        break
                return bestScore, bestMove
            else:
                bestScore = float("inf")
                bestMove = None
                for move in board.legal_moves:
                    board.push(move)
                    move_value, _ = alphabeta(board, depth - 1, True, alpha, beta)
                    board.pop()
                    if move_value < bestScore:
                        bestScore = move_value
                        bestMove = move
                    beta = min(beta, move_value)
                    if beta <= alpha:
                        break
                return bestScore, bestMove

    answer = alphabeta(board, N, maximizing_player=board.turn==chess.WHITE)
    print("Nodes expanded: %d" %(nodes_expanded))
    return answer
