import random
import math
from MCTSNode import MCTSNode


def calcUCB1(node, parent):
    if node.visit_count == 0:
        return math.inf
    return node.value() + 2 * math.sqrt(math.log(parent.visit_count) / node.visit_count)


def MCTSRoot(root_state, max_visits=500):
    root = MCTSNode(root_state)
    root.expandChildren()
    for _ in range(max_visits):
        to_expand = selectChild(root)
        root.value_sum += MCTS(to_expand)
        root.visit_count += 1
    return root


def MCTS(node):
    node.transitionWithMove()
    if node.visit_count == 0 and not node.isGameTerminal():
        result = RolloutNode(node.gamestate)
        node.expandChildren()
        node.undoMoveTransition()
        node.value_sum += result
        node.visit_count += 1
    elif not node.isGameTerminal():
        to_expand = selectChild(node)
        result = MCTS(to_expand)
        node.undoMoveTransition()
        node.value_sum += result
        node.visit_count += 1
    else:  # Game terminal node
        result = RolloutNode(node.gamestate)
        node.undoMoveTransition()
        node.value_sum += result
        node.visit_count += 1
    return result


def selectChild(node):
    max_ucb1 = -math.inf
    best_node = []
    for child in node.children:
        child_ucb1 = calcUCB1(child, node)
        if max_ucb1 < child_ucb1:
            best_node = [child]
        elif max_ucb1 == child_ucb1:
            best_node.append(child)
        max_ucb1 = max(max_ucb1, child_ucb1)
    return random.choice(best_node)


def RolloutNode(gamestate):
    if gamestate.is_game_over():
        return resultBlackPerspective(gamestate.result())
    else:
        moves = [move for move in gamestate.legal_moves]
        move = random.choice(moves)
        gamestate.push(move)
        result = RolloutNode(gamestate)
        gamestate.pop()
        return result


def resultBlackPerspective(result):
    if result == "1-0":
        return 1
    elif result == "0-1":
        return -1
    return 0


def backPropagateRollout(node, value):
    node.value_sum += value
    node.visit_count += 1
    if node.parent is not None:
        backPropagateRollout(node.parent, value)
