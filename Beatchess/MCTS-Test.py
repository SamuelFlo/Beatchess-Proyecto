import chess
import MCTS

def main():
    board = chess.Board()
    print(board)
    results = MCTS.MCTSRoot(board)
    for child in results.children:
        print(child.visit_count)
    print(f"Max: {results.getMostVisitedChild().visit_count}")
    print(results.getMostVisitedChild().move)


if __name__ == "__main__":
    main()