import chess

PIECES = chess.PIECE_TYPES

columns = ['wMate', 'bMate', 'draw', 'turn', 
           'wP','wN','wB','wR','wQ','wK','bP','bN','bB','bR','bQ','bK',
           'hwP','hwN','hwB','hwR','hwQ','hwK','hbP','hbN','hbB','hbR','hbQ','hbK',
          'EVAL']
def boardfeatures(board):
    """
    Feature containing castling rights, turn, and every possible piece type belonging in every possible square
    """
    featuresList = []
    featuresList.append(currentTurn(board))
    featuresList.extend(castlingRights(board))
    featuresList.extend(PList(containsPCinSquare, board))
    return featuresList
    

def features(board):
    """
    Returns a list of numerical values for features of a board. Subject to change.
    [ischeckmate[W/B], isDraw, turn, material[PNBRKQ][W/B] ,hangingMaterial[W/b]]
    """
    featuresList = []
    featuresList.extend(colorList(isCheckmate, board))
    featuresList.extend([isDraw(board)])
    featuresList.extend([currentTurn(board)])
    featuresList.extend(pieceColorList(numPieceOfColor, board))
    featuresList.extend(pieceColorList(numHangingPieceOfColor, board))
    return featuresList
    
def containsPCinSquare(board, piece, color, square):
    if board.color_at(square) == color and board.piece_type_at(square) == piece:
        return 1
    return 0

def PCSList(fn, board, piece, color):
    a = [fn(board, piece, color, square) for square in chess.SQUARES]
    return a

def PCList(fn, board, piece):
    a = PCSList(fn, board, piece, chess.WHITE)
    b = PCSList(fn, board, piece, chess.BLACK)
    a.extend(b)
    return a

def PList(fn, board):

    lists = [PCList(fn, board, piece) for piece in chess.PIECE_TYPES]
    answer = []
    for i in lists:
        answer.extend(i);
    return answer
    
def castlingRights(board):
    return [int(board.has_kingside_castling_rights(chess.WHITE)), 
           int(board.has_queenside_castling_rights(chess.WHITE)),
           int(board.has_kingside_castling_rights(chess.BLACK)),
           int(board.has_queenside_castling_rights(chess.BLACK))]


def pieceColorList(fn, board):
    """
    Returns a list containing FN called on every piece type and color combo
    """
    a = [fn(board, piece, chess.WHITE) for piece in PIECES]
    a.extend([fn(board, piece, chess.BLACK) for piece in PIECES])
    return a
    
def colorList(fn, board):
    """
    Returns a list containing FN called on both color
    """
    a = [fn(board, chess.WHITE)]
    a.extend([fn(board, chess.BLACK)])
    return a
    
def isCheckmate(board, color):
    """
    Returns 1 if the current color is checkmating the other
    """
    if board.is_checkmate() and board.turn == (not color):
        return 1
    return 0

def isDraw(board):
    """
    Returns 1 iff the current position is a draw
    """
    if board.result() == '1/2-1/2': #might have to input some * in result
        return 1
    return 0

def currentTurn(board):
    if board.turn == chess.WHITE:
        return 1
    return 0

def numPieceOfColor(board, piece, color):
    """
    Returns the number of pieces of specific color
    """
    return len(board.pieces(piece, color))

def numHangingPieceOfColor(board, piece, color): 
    #Update function to still count pieces as hanging if num attacker pawns > defender pawns, repeat for each piece...
    """
    Returns the number of hanging pieces of a specific color 
    """
    our_pieces = board.pieces(piece, color)
    opp_color = not color
    hanging_pieces = 0
    for sq in our_pieces:
        unpinned_attackers_on_sq = sum([not board.is_pinned(not color, opp_att) for opp_att in board.attackers(opp_color, sq)])
        unpinned_defenders_on_sq = sum([not board.is_pinned(color, opp_att) for opp_att in board.attackers(color, sq)]) 
        if unpinned_attackers_on_sq > unpinned_defenders_on_sq:
            hanging_pieces += 1
    return hanging_pieces
