import chess
import MCTS

def main():
    board = chess.Board()
    results = MCTS.MCTSRoot(board)
    for child in results.children:
        print(child.visit_count)
    print(f"Max: {results.getMostVisitedChild().visit_count}")


if __name__ == "__main__":
    main()