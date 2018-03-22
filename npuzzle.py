# N Puzzle
# A* or Best First Search
# Python 3

from agent import Agent
from state import State


def main():
    start = State(3)
    start.shuffle()
    while not start.isSolvable():
        start.shuffle()

    goal3 = State(3,
                 [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])
    a = Agent()
    a.gDebug = False

    print("N Puzzle")
    print("A* or Best First Search\n")
    searchType = input("A*/Best First (a/b):")
    if searchType == "a":
        astar = True
    else:
        astar = False

    heuristicType = input("Manhattan Distance/Misplaced Tiles (d/t):")
    if heuristicType == "d":
        heuristic = "manhattan"
    else:
        heuristic = "misplaced"

    print("Searching for solution...")
    solution = a.search(start, goal3, astar, heuristic)
    if solution:
        print("Solution found!")
        solution.traceBack()
        a.getMetrics(solution)
    else:
        print("No solution found!")


if __name__ == "__main__":
    main()
