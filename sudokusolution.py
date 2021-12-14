import time

class Sudoku:
    def __init__(self, sudoku=None):
        if sudoku is None:
            sudoku = [[]]
        self.sudoku = sudoku
        self.pairs = []
        self.emptylist()

    def emptylist(self):
        for row in range(9):
            for col in range(9):
                if self.sudoku[row][col] == 0:
                    self.pairs.append([row, col])
        return

    def checksudoku(self, ind):
        for i in range(9):
            if self.sudoku[self.pairs[ind][0]][self.pairs[ind][1]] == self.sudoku[self.pairs[ind][0]][i] and i != \
                    self.pairs[ind][1]:
                return False
            if self.sudoku[self.pairs[ind][0]][self.pairs[ind][1]] == self.sudoku[i][self.pairs[ind][1]] and i != \
                    self.pairs[ind][0]:
                return False
        x = self.pairs[ind][0] - self.pairs[ind][0] % 3
        y = self.pairs[ind][1] - self.pairs[ind][1] % 3
        for i in range(3):
            for j in range(3):
                if self.pairs[ind] == [x + i, y + j]:
                    continue
                if self.sudoku[x + i][y + j] == self.sudoku[self.pairs[ind][0]][self.pairs[ind][1]]:
                    return False
        return True

    def solution(self, ind=0):
        if ind == len(self.pairs):
            return True
        for i in range(9):
            self.sudoku[self.pairs[ind][0]][self.pairs[ind][1]] = i + 1
            if self.checksudoku(ind):
                if self.solution(ind + 1):
                    return True
        self.sudoku[self.pairs[ind][0]][self.pairs[ind][1]] = 0
        return False

    def printsudoku(self):
        for i in range(9):
            print(self.sudoku[i])
        return


def main():
    start_time = time.time()
    example = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 3, 6, 0, 0, 0, 0, 0],
               [0, 7, 0, 0, 9, 0, 2, 0, 0],
               [0, 5, 0, 0, 0, 7, 0, 0, 0],
               [0, 0, 0, 0, 4, 5, 7, 0, 1],
               [0, 0, 0, 1, 0, 0, 0, 3, 0],
               [0, 0, 1, 0, 0, 0, 0, 6, 8],
               [0, 0, 8, 5, 0, 0, 0, 1, 0],
               [0, 9, 0, 0, 0, 0, 4, 0, 0]]
    my_sudoku = Sudoku(example)
    print(my_sudoku.solution())
    my_sudoku.printsudoku()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
