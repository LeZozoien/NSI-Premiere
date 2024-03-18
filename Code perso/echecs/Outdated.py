class inputError(BaseException):
    def __init__(self, leng, expleng) -> None:
        super().__init__(f"Wrong input length ({leng}) expected {expleng}")

def index(case:str)->int:

    """
    get an index (8) from a square code (H1)

    >>> index("f8")
    48

    >>> index("b3")
    17
    """
    case = case.lower().strip()
    if len(case) > 2:
        raise inputError(len(case), 2)
    index_letters = {"a" : 0, "b" : 1, "c" : 2, "d" : 3,
                     "e" : 4, "f" : 5, "g" : 6, "h" : 7,}
    return index_letters[case[0]] + (int(case[1])-1)*8

def pos_to_bitboard(*squares):
    squares_indexes = [index(square) for square in squares]
    squares_indexes.sort()

    bitboard = 0

    for i in squares_indexes:
        bitboard += 2**i

    return bitboard

def init_board(board):
    board["whitePawns"] = pos_to_bitboard("a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2")
    board["whiteKnights"] = pos_to_bitboard("b1", "g1")
    board["whiteBishops"] = pos_to_bitboard("c1", "f1")
    board["whiteRooks"] = pos_to_bitboard("a1", "h1")
    board["whiteQueens"] = pos_to_bitboard("d1")
    board["whiteKing"] = pos_to_bitboard("e1")
    board["blackPawns"] = pos_to_bitboard("a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7")
    board["blackKnights"] = pos_to_bitboard("b8", "g8")
    board["blackBishops"] = pos_to_bitboard("c8", "f8")
    board["blackRooks"] = pos_to_bitboard("a8", "h8")
    board["blackQueens"] = pos_to_bitboard("d8")
    board["blackKing"] = pos_to_bitboard("e8")

def determine_piece(board:dict, index):
    for i in range(12):
        result = list(board.values())[i] & (2**index)
        match result:
            case 0:
                pass
            case _:
                return list(board.keys())[i]
    return 0

def print_board(board):
    print("┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐")
    for y in range(7):
        print("│", end="  ")
        for x in range(8):
            print(SYMBOLES[determine_piece(board, 56-y*8+x)], end="  │  ")
        print()
        print("├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
    print("│", end="  ")
    for x in range(8):
        print(SYMBOLES[determine_piece(board, 56-7*8+x)], end="  │  ")
    print()
    print("└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘")

board = {
    "whitePawns" : 0,
    "whiteKnights" : 0,
    "whiteBishops" : 0,
    "whiteRooks" : 0,
    "whiteQueens" : 0,
    "whiteKing" : 0,
    "blackPawns" : 0,
    "blackKnights" : 0,
    "blackBishops" : 0,
    "blackRooks" : 0,
    "blackQueens" : 0,
    "blackKing" : 0}

SYMBOLES = {
    "whitePawns" : "P",
    "whiteKnights" : "N",
    "whiteBishops" : "B",
    "whiteRooks" : "R",
    "whiteQueens" : "Q",
    "whiteKing" : "K",
    "blackPawns" : "p",
    "blackKnights" : "n",
    "blackBishops" : "b",
    "blackRooks" : "r",
    "blackQueens" : "q",
    "blackKing" : "k",
    0 : " "}

init_board(board)

print_board(board)