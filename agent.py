import frontier
import exploredset
from node import Node


class Agent:
    gDebug = False

    def __init__(self):
        self.frontier = frontier.Frontier()
        self.exset = exploredset.ExploredSet()
        self.numnodes = 0

    def search(self, start, goal, astar, heuristic):
        if heuristic == "manhattan":
            h = start.manhattanDist(goal)
        elif heuristic == "misplaced":
            h = start.misplacedTiles(goal)
        else:
            print("Invalid heuristic!")
            print("Try: 'manhattan' or 'misplaced'")
            return None

        self.frontier.add(Node(None, start, 0, h))

        while True:

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
                    h = neighbor.misplacedTiles(goal)

                if astar:
                    h += p.getPathlen() + 1
                n = Node(p, neighbor, 1, h)
                self.numnodes += 1

                if not self.exset.check(n):
                    self.frontier.add(n)

    def getMetrics(self, solution):
        print(" --- Metrics -----")
        print("Path length:", solution.getPathlen())
        print("Explored nodes:", len(self.exset))
        print("Nodes in frontier:", len(self.frontier))
        print("Created nodes:", self.numnodes)

