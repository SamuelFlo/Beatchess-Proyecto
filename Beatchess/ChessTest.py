import chess

from AlphaBetaPruning import ABPruningAI
import time

def main():
    AI = ABPruningAI()
    turn = 1
    board = chess.Board()
    while True:
        print(f"Turn {turn}")
        print(board)
        move = input("Type your move: ")
        board.push(chess.Move.from_uci(move))
        print(board)
        print('-'*60)
        #time.sleep(3)
        ai_move = AI.BestMove(board)
        board.push(ai_move)
        print(ai_move)
        turn += 1


if __name__ == "__main__":
    main()
