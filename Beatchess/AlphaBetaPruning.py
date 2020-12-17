from math import inf
import numpy as np
import random

class ABPruningAI:

    def __init__(self, depth_limit=2):
        self.depth_limit = depth_limit
        self.pieceValues = {}
        self.initPieceValues()
        self.explorados = 0

    def BestMove(self, current_state):
        return self.AlphaBetaPruning(current_state)

    def AlphaBetaPruning(self, current_state, depth=0, maximizingTurn=True, alpha=-inf, beta=inf):
        if depth == self.depth_limit or self.GameOver(current_state):
            return self.leafStateValue(current_state)
        elif maximizingTurn:
            max_value = -inf
            max_move = None  # Needed to return the most promising move
            moves = [move for move in current_state.legal_moves]
            random.shuffle(moves)
            for move in moves:  # Could be improved with move ordering
                self.explorados += 1
                current_state.push(move)  # Move piece to explore new state
                value = self.AlphaBetaPruning(current_state, depth + 1, not maximizingTurn, alpha, beta)
                max_value = max(max_value, value)
                alpha = max(alpha, max_value)
                if max_value == value:
                    max_move = move
                current_state.pop()  # Undo previous move to return to the previous state
                if beta <= alpha:
                    break
            if depth == 0:
                print(self.explorados)
                print(max_value)
                return max_move
            else:
                return max_value
        else:
            min_value = inf
            moves = [move for move in current_state.legal_moves]
            random.shuffle(moves)
            for move in moves:
                self.explorados += 1
                current_state.push(move)  # Move piece to explore new state
                value = self.AlphaBetaPruning(current_state, depth + 1, not maximizingTurn, alpha, beta)
                min_value = min(min_value, value)
                beta = min(beta, min_value)
                current_state.pop()  # Undo previous move to return to the previous state
                if beta <= alpha:
                    break
            return min_value

    def leafStateValue(self, current_state):
        value = 0
        x, y = 0, 0
        for char in current_state.fen().split()[0]:
            if char in self.pieceValues.keys():
                value += self.pieceValues[char][x][y]
                y += 1
            elif char == '/':
                x += 1
                y = 0
            else:
                y += int(char)
        return value

    def GameOver(self, current_state):
        return False

    def initPieceValues(self):
        # Initialize pawn values
        self.pieceValues["P"] = -10 - np.array([
            [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
            [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
            [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
            [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
            [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
            [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
            [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
            [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
        ])
        self.pieceValues["p"] = -self.pieceValues["P"][::-1]

        # Initialize knight values
        self.pieceValues["N"] = -30 - np.array([
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
            [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
            [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
            [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
            [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
            [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
            [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
        ])
        self.pieceValues["n"] = -self.pieceValues["N"]

        # Initialize bishop values
        self.pieceValues["B"] = -30 - np.array([
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
            [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
            [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
            [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
            [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
            [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
        ])
        self.pieceValues["b"] = -self.pieceValues["B"][::-1]

        # Initialize rook values
        self.pieceValues["R"] = -50 - np.array([
            [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
            [0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
        ])
        self.pieceValues["r"] = -self.pieceValues["R"][::-1]

        # Initialize queen values
        self.pieceValues["Q"] = -90 - np.array([
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
            [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
            [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
            [0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
            [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
        ])
        self.pieceValues["q"] = -self.pieceValues["Q"].copy()

        # Initialize queen values
        self.pieceValues["K"] = -900 - np.array([
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
            [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
            [2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
            [2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
        ])
        self.pieceValues["k"] = -self.pieceValues["K"][::-1]
