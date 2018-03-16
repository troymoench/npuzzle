from random import shuffle
import copy


class State:
    def __init__(self, n, board=None):
        self.n = n
        if board is None:
            self.board = [[0]*n for _ in range(n)]
        else:
            self.board = board

    def __eq__(self, other):
        return self.board == other.board

    def shuffle(self):
        nums = list(range(self.n*self.n))
        shuffle(nums)

        for i in range(self.n):
            for j in range(self.n):
                self.board[i][j] = nums.pop()

    def isSolvable(self):
        flat_board = [item for sublist in self.board for item in sublist]
        SZ = self.n
        count = 0
        thiscnt = 0

        bp = 0
        last = len(flat_board) - 1
        blankRowFromBottom = 0
        gridWidthOdd = SZ % 2
        # the score of the last cell is always 0, so don't visit
        for i in range(SZ * SZ - 1):
            curval = flat_board[bp]
            bp += 1
            if curval == 0:
                blankRowFromBottom = (SZ - 1) - (i / SZ)
                continue
            tmpp = bp
            thiscnt = 0
            while tmpp <= last:
                if (flat_board[tmpp] != 0) and (flat_board[tmpp] < curval):
                    thiscnt += 1

                tmpp += 1
            count += thiscnt
        inversionsEven = (count % 2 == 0)
        blankOddFromBottom = (blankRowFromBottom % 2 == 0)

        if (gridWidthOdd and inversionsEven) or \
                (not gridWidthOdd and (blankOddFromBottom == inversionsEven)):
            return True
        else:
            return False

    def getCell(self, row, col):
        return self.board[row][col]

    def findCell(self, value):
        # return coordinates of cell value
        for row in range(self.n):
            if value in self.board[row]:
                col = self.board[row].index(value)
                return row, col
        return None

    def findNeighbors(self):
        # return list of neighboring states
        # check left, right, up, down
        neighbors = []

        # get position of blank
        i, j = self.findCell(0)
        board = copy.deepcopy(self.board)

        # check up
        if i - 1 >= 0:
            # print("Up")
            pos = i - 1
            board[i][j], board[pos][j] = board[pos][j], board[i][j]
            neighbors.append(State(self.n, board))
            # reset board
            board = copy.deepcopy(self.board)

        # check down
        if i + 1 < self.n:
            # print("Down")
            pos = i + 1
            board[i][j], board[pos][j] = board[pos][j], board[i][j]
            neighbors.append(State(self.n, board))
            # reset board
            board = copy.deepcopy(self.board)

        # check left
        if j - 1 >= 0:
            # print("Left")
            pos = j - 1
            board[i][j], board[i][pos] = board[i][pos], board[i][j]
            neighbors.append(State(self.n, board))
            # reset board
            board = copy.deepcopy(self.board)

        # check right
        if j + 1 < self.n:
            # print("Right")
            pos = j + 1
            board[i][j], board[i][pos] = board[i][pos], board[i][j]
            neighbors.append(State(self.n, board))

        return neighbors

    def print(self):
        for i in range(self.n):
            print(" ".join(map(str, self.board[i])))


if __name__ == "__main__":
    st = State(4)
    st.print()
    st.shuffle()
    st.print()
    print(st.isSolvable())

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

    print("solvable" if goalA.isSolvable() else "not solvable")
    print("solvable" if goalB.isSolvable() else "not solvable")
    print("solvable" if testA.isSolvable() else "not solvable")
    print(goalA == goalB)
    print(goalA == goalA)
    print(goalA.getCell(1, 2))
    print(goalA.findCell(0))

    neighbors = goalB.findNeighbors()
    for neighbor in neighbors:
        neighbor.print()
