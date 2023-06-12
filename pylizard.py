## Pylizard is a Python 3.6+ library for interacting with the Lizard API.
print("Hello World!")

# function to connect with Lizard API
def connect():
    print("Connecting to Lizard API...")

# dit is echt onzin

## Chess Piece Class
class ChessPiece:
    def __init__(self, color, pieceType):
        self.color = color
        self.pieceType = pieceType
        self.position = None

    def move(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def getColor(self):
        return self.color

    def getPieceType(self):
        return self.pieceType

    def __str__(self):
        return self.color + " " + self.pieceType