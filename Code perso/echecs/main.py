import pygame


class Piece:
    NONE = 0; KING = 1; PAWN = 2; KNIGHT = 3; BISHOP = 4; ROOK = 5; QUEEN = 6

    WHITE = 8; BLACK = 16

    def toName(number):
        piece = ""
        match number%8:
            case 0: return ' '
            case 1: piece += "k"
            case 2: piece += "p"
            case 3: piece += "n"
            case 4: piece += "b"
            case 5: piece += "r"
            case 6: piece += "q"
        if Piece.isColour(number, Piece.WHITE):
            piece = piece.upper()
        return piece
    
    def isColour(piece, colour):
        piececolour = piece//8 * 8
        return piececolour == colour

    def isSlidingPiece(arg):
        if isinstance(arg, Piece):
            if arg.isType(Piece.BISHOP) or arg.isType(Piece.ROOK) or arg.isType(Piece.QUEEN):return True
            else: return False
    
    def isType(piece, type): return piece % 8 == type

class Board(list):
    def __init__(self):
        self.clear()
        for i in range(64):
            self.append(Piece.NONE)

        self.colourToMove = Piece.WHITE

    STARTFEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

    pieceTypeFromSymbol = {'k' : Piece.KING, 'p' : Piece.PAWN, 'n' : Piece.KNIGHT,
                           'b' : Piece.BISHOP, 'r' : Piece.ROOK, 'q' : Piece.QUEEN}

    def loadPositionFromFen(self, fen:str):
        fenBoard = fen.split()[0]
        file, rank = 0, 7

        for symbol in fenBoard:
            if symbol == '/':
                file = 0; rank -= 1
            elif symbol.isdigit():
                file += int(symbol)
            else:
                pieceColor = [Piece.WHITE, Piece.BLACK][symbol.isupper()]
                pieceType = self.pieceTypeFromSymbol[symbol.lower()]
                board[8*rank + file] = pieceType | pieceColor
                file += 1

    def __repr__(self):
        buf1 = ""
        for x in range(8):
            for y in range(8):
                buf1 += Piece.toName(self[8*x+y]) + "  "
            buf1 += '\n'
        return buf1

class Move:
    def __init__(self, startSquare, targetSquare) -> None:
        self.startSquare = startSquare
        self.targetSquare = targetSquare
    
    def __repr__(self) -> str:
        return indexToCode(self.startSquare) + " -- " + indexToCode(self.targetSquare)

def draw_board(screen:pygame.Surface):
    for y in range(8):
        for x in range(8):

            isLightSquare = (x+y)%2 == 0

            if isLightSquare:
                pygame.draw.rect(screen, WHITE, (x*SQ_SIZE, y*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                pygame.draw.rect(screen, BLACK, (x*SQ_SIZE, y*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def indexToCode(index):
    digit = index//8 +1
    letter = chr(96+index%8)
    return letter + str(digit)

def precomputedMoveData():
    buf = [[0 for i in range(8)] for j in range(64)]

    for file in range(8):
        for rank in range(8):

            numNorth = 7 - rank
            numSouth = rank
            numWest = file
            numEast = 7 - file

            squareIndex = rank * 8 + file

            buf[squareIndex] = [
                numNorth,
                numSouth,
                numWest,
                numEast,
                min(numNorth, numWest),
                min(numSouth, numEast),
                min(numNorth, numEast),
                min(numSouth, numWest)
            ]
    return buf
squaresToEdge = precomputedMoveData()

def generateMoves(board:Board):
    for startSquare in range(64):
        piece = board[startSquare]
        if Piece.isColour(piece, board.colourToMove):
            if Piece.isSlidingPiece(piece):
                generateSlidingMoves(startSquare, piece)
            elif Piece.isType(piece, Piece.PAWN):
                generatePawnMoves(startSquare)

def generateSlidingMoves(piece, startSquare):
    startDirIndex = (Piece.isType(piece, Piece.BISHOP))*4
    endDirIndex = 8-(Piece.isType(piece, Piece.ROOK))*4

    for directionindex in range(startDirIndex, endDirIndex, 1):
        for n in range(squaresToEdge[startSquare][directionindex]):
            target = startSquare + DirectionOffsets[directionindex] * (n + 1)
            pieceOnTargetSquare = board[target]

            if Piece.isColour(pieceOnTargetSquare, board.colourToMove):
                break

            moves.append(Move(startSquare, target))

            if not Piece.isColour(pieceOnTargetSquare, board.colourToMove):
                break

def generatePawnMoves(startSquare):
    target = startSquare + DirectionOffsets[0]
    pieceOnTargetSquare = board[target]

    if Piece.isColour(pieceOnTargetSquare, board.colourToMove):
        pass
    else: moves.append(Move(startSquare, target))

DirectionOffsets = [8, -8, -1, 1, 7, -7, 9, -9]

moves = []

board = Board()

pygame.init()

BGCOLOR = (100, 100, 100)
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)

WINDOWSIZE = WIDTH, HEIGHT = (500, 500)
HALFW, HALFH = WIDTH/2, HEIGHT/2
SQ_SIZE = WIDTH / 8

screen = pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption("Echecs")

running = True

board.loadPositionFromFen(board.STARTFEN)

generateMoves(board)

print(moves)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BGCOLOR)

    draw_board(screen)
    pygame.display.flip()