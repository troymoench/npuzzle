# Cannibals and Missionaries
# Breadth First Search
# Python 3

from agent import Agent
from state import State


def main():
    start = State(3)
    start.shuffle()
    while not start.isSolvable():
        start.shuffle()

    goal = State(3,
                 [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])
    a = Agent()
    a.gDebug = False
    print("N Puzzle")
    print("Best First or A* Search\n")
    print("Searching for solution...")
    solution = a.search(start, goal, False, "manhattan")
    if solution:
        print("Solution found!")
        solution.traceBack()
    else:
        print("No solution found!")


if __name__ == "__main__":
    main()
