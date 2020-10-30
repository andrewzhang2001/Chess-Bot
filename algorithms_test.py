from algorithms import naive_alphabeta
import chess

def test_alphabeta(ab_func, board, N, board_eval_func):
    """
    Generic testing function for an alpha beta algorithm.
    """
    ab_score, ab_move = ab_func(board, N, board_eval_func)
    print("Alpha Beta search results Best Move: %s. Score: %f.\n" %(ab_move, ab_score))

def test_one():
    board = chess.Board()
    def eval_func():
        return 2
    test_alphabeta(naive_alphabeta, board, 3, eval_func)

if __name__ == "__main__":
    test_one()
