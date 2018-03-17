import frontier
import exploredset
from node import Node


class Agent:
    gDebug = False

    def __init__(self):
        self.frontier = frontier.Frontier()
        self.exset = exploredset.ExploredSet()

    def search(self, start, goal, astar, heuristic):
        if heuristic == "manhattan":
            h = start.manhattanDist(goal)
        elif heuristic == "misplaced":
            h = start.misplaced(goal)
        else:
            print("Invalid heuristic!")
            print("Try: 'manhattan' or 'misplaced'")
            return None

        self.frontier.add(Node(None, start, 0, h))

        count = 0
        while True:
            print("\nRound:", count, "\n")
            print("Size of frontier:", len(self.frontier.fnodes))
            print("Size of exset:", len(self.exset.exset))
            if self.gDebug:
                self.frontier.print()
                self.exset.print()

            if self.frontier.isEmpty():
                return None
            p = self.frontier.pop()
            if p.getState() == goal:
                return p
            self.exset.add(p)

            # find neighboring states
            neighbors = p.getState().findNeighbors()

            for neighbor in neighbors:
                if heuristic == "manhattan":
                    h = neighbor.manhattanDist(goal)
                elif heuristic == "misplaced":
                    h = neighbor.misplaced(goal)

                n = Node(p, neighbor, 1, h)

                if not self.exset.check(n):
                    self.frontier.add(n)
            count += 1
