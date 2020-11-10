from src.algorithms import naive_alphabeta
from test.test_library import test_search
import unittest
import chess

def test_alphabeta(ab_func, board, N, board_eval_func):
    """
    Generic testing function for an alpha beta algorithm.
    """
    ab_score, ab_move = ab_func(board, N, board_eval_func)
    print(ab_func.__name__+" search results Best Move: %s. Score: %f." %(ab_move, ab_score))

@test_search
def test_one():
    board = chess.Board()
    def eval_func():
        return 2
    test_alphabeta(naive_alphabeta, board, 3, eval_func)


class TestOne(unittest.TestCase):
    test_one()
