import chess
import MCTS

def main():
    board = chess.Board('4q2k/2r1r1p1/4Pn1p/p1p2R2/P2pQ2P/1P1B1R2/6P1/6K1 w - - 9 38')
    print(board)
    #results = MCTS.MCTSRoot(board)
    #for child in results.children:
    #    print(child.visit_count)
    #print(f"Max: {results.getMostVisitedChild().visit_count}")
    #print(results.getMostVisitedChild().move)
    print(getPieceIn('f5', board.fen()))

def getPieceIn(position, fen):
    i, j = toNumeric(position)
    j = 7 - j
    trim = fen.split()
    board = trim[0].split('/')
    for _, char in enumerate(board[j]):
        if i < 0:
            return 0
        if char.isnumeric():
            if i == 0:
                return getPieceVal(char)
            i -= int(char)
            continue
        if i == 0:
            return getPieceVal(char)
        i -= 1


def getPieceVal(char):
    if char == 'P':
        return 1
    if char == 'p':
        return -1
    if char == 'N':
        return 2
    if char == 'n':
        return -2
    if char == 'B':
        return 3
    if char == 'b':
        return -3
    if char == 'K':
        return 100
    if char == 'k':
        return -100
    if char == 'Q':
        return 9
    if char == 'q':
        return -9
    if char == 'R':
        return 5
    if char == 'r':
        return -5
    return 0

def toNumeric(position):
    i = -1
    if position[0] == 'a':
        i = 0
    elif position[0] == 'b':
        i = 1
    elif position[0] == 'c':
        i = 2
    elif position[0] == 'd':
        i = 3
    elif position[0] == 'e':
        i = 4
    elif position[0] == 'f':
        i = 5
    elif position[0] == 'g':
        i = 6
    elif position[0] == 'h':
        i = 7
    return i, int(position[1]) - 1

if __name__ == "__main__":
    main()


