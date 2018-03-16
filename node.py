from state import State


class Node:
    def __init__(self, n, state, ucost, fcost):
        self.parent = n
        self.state = state
        self.ucost = ucost
        self.pcost = 0
        if self.parent:
            self.pcost = self.parent.pcost
        self.fcost = fcost

    def __eq__(self, other):
        return self.state == other.state

    def __lt__(self, other):
        return self.fcost < other.fcost

    def __gt__(self, other):
        return self.fcost > other.fcost

    def print(self):
        print("State:")
        self.state.print()
        print("pcost:", self.pcost)
        print("fcost:", self.fcost)

    def eval(self):
        return self.fcost

    def getState(self):
        return self.state

    def traceBack(self):
        nodes = []

        nodes.append(self)

        p = self.parent
        while p:
            nodes.append(p)
            p = p.parent

        nodes.reverse()
        for node in nodes:
            node.print()


if __name__ == "__main__":
    goalA = State(3,
                  [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]])
    goalB = State(3,
                  [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 0]])

    testA = State(3,
                  [[1, 2, 3],
                   [8, 0, 4],
                   [7, 6, 5]])

    n = Node(None, goalA, 1, 5)
    n.print()
