import chess
import math
import random

class MCTSNode:

    def __init__(self, gamestate, move=None, parent=None):
        self.parent = parent
        self.children = []
        self.visit_count = 0
        self.value_sum = 0
        self.gamestate = gamestate
        self.move = move

    def value(self):
        return self.value_sum / self.visit_count

    def expandChildren(self):
        for move in self.gamestate.legal_moves:
            self.children.append(MCTSNode(self.gamestate, move))

    def transitionWithMove(self):
        if self.move is not None:
            self.gamestate.push(self.move)

    def undoMoveTransition(self):
        if self.move is not None:
            self.gamestate.pop()

    def isGameTerminal(self):
        return self.gamestate.is_game_over() or self.gamestate.is_stalemate()

    def getMostVisitedChild(self):
        max_visited = -math.inf
        nodes = []
        for child in self.children:
            if child.value() > max_visited:
                nodes = [child]
                max_visited = child.value()
            elif child.visit_count == max_visited:
                nodes.append(child)
        return random.choice(nodes)
