from node import Node
from state import State


class Frontier:
    def __init__(self):
        self.fnodes = []

    def __len__(self):
        return len(self.fnodes)

    def add(self, n):

        p = 0
        q = None
        while (p < len(self.fnodes)) and (n > self.fnodes[p]):
            q = p
            p += 1

        # Insert at the head
        if q is None:
            self.fnodes.insert(0, n)
        else:
            self.fnodes.insert(p, n)

    def pop(self):
        return self.fnodes.pop(0)

    def isEmpty(self):
        return len(self.fnodes) == 0

    def check(self, n):
        return n in self.fnodes

    def print(self):
        print("<Frontier>")
        for n in self.fnodes:
            n.print()
        print("</Frontier>")


if __name__ == "__main__":
    f = Frontier()
    goalA = State(3,
                  [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]])

    n = Node(None, goalA, 1, 5)

    # n.print()
    f.add(n)
    # f.print()
    f.add(Node(None, goalA, 1, 3))
    # f.print()
    f.add(Node(None, goalA, 1, 7))
    # f.print()
    f.add(Node(None, goalA, 1, 4))
    f.add(Node(None, goalA, 1, 6))
    f.print()

    print(f.check(n))
    f.pop()
    f.print()
