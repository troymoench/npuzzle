import node


class ExploredSet:
    def __init__(self):
        self.exset = []

    def add(self, n):
        self.exset.append(n)

    def check(self, n):
        return n in self.exset

    def print(self):
        print("<EX>")
        for n in self.exset:
            n.print()
        print("</EX>")


if __name__ == "__main__":
    exset = ExploredSet()
    exset.print()
