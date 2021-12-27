from run import run

class clr:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DIM = f'\u001b[38;5;{239}m'
    DIMBG = f'\u001b[48;5;{236}m'

class Bingo:
    def __init__(self, text):
        self.grid = []
        lines = text.split('\n')
        for line in lines:
            cells = line.split(' ')
            cells = filter(lambda cell:len(cell) > 0, cells)
            cells = list(map(int, cells))
            self.grid.append(cells)
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def print(self, callouts=[]):
        isWinner = self.hasWon(callouts)
        for row in self.grid:
            cells = map(lambda cell: str(cell), row)
            cells = map(lambda cell: cell.rjust(2), cells)
            highlight = ('',clr.DIMBG)[isWinner]
            cells = map(lambda cell: (f'{highlight}{clr.DIM}{cell}{clr.RESET}',f'{highlight}{clr.BOLD}{cell}{clr.RESET}')[int(cell) in callouts], cells)
            cells = f'{highlight} {clr.RESET}'.join(cells)
            print(cells)

    def hasWon(self, callouts):
        # check rows
        for row in self.grid:
            count = 0
            for cell in row:
                if cell in callouts:
                    count += 1
            if count == self.width:
                return True

        # check columns
        for i in range(0,self.width):
            count = 0;
            for row in self.grid:
                cell = row[0]
                if (cell in callouts):
                    count += 1
            if count == self.height:
                return True

        # nothing found, no winners yet
        return False

    def umarkedCells(self, callouts):
        cells = []
        for row in self.grid:
            for cell in row:
                if (cell in callouts) == False:
                    cells.append(cell)
        return cells



def printBoards(boards, callouts=[]):
    for i, board in enumerate(boards):
        print()
        print(clr.HEADER + f'Board {i+1}'.center(14) + clr.RESET)
        board.print(callouts)

def solve(input: str):
    sections = input.split("\n\n")

    callouts = list(map(int, sections.pop(0).split(',')))
    print(callouts)

    boards = list(map(lambda text : Bingo(text), sections))
    # printBoards(boards)

    hasWinner = False
    calloutIndex = 0
    totalCalloutCount = len(callouts)
    unmarkedSum = 0
    while hasWinner == False and calloutIndex < totalCalloutCount:
        currentCallouts = callouts[0:calloutIndex]
        for board in boards:
            isWinner = board.hasWon(currentCallouts)
            if isWinner:
                unmarkedSum = sum(board.umarkedCells(currentCallouts))
                hasWinner = True
                break
        calloutIndex += 1

    winningCallout = callouts[calloutIndex-2]
    printBoards(boards, currentCallouts)

    print()
    print(f'   Unmarked sum: {unmarkedSum}')
    print(f'Winning callout: {winningCallout}')

    return winningCallout * unmarkedSum


if __name__ == "__main__":
    run(solve, 4, 1)
