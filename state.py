from random import shuffle


class State:
    def __init__(self, n, board=None):
        self.n = n
        if board is None:
            self.board = [[0]*n for _ in range(n)]
        else:
            self.board = board

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
        # tmpp
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

    def print(self):
        for i in range(self.n):
            print(" ".join(map(str, self.board[i])))


if __name__ == "__main__":
    st = State(3)
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
