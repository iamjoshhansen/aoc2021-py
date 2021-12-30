from collections import namedtuple

Cell = namedtuple('Cell', 'x y')
CellAndValue = namedtuple('CellAndValue', 'cell value')


class Grid2D:
    def __init__(self, values2D=[]):
        self.values2D = values2D
        self.width = len(values2D[0])
        self.height = len(values2D)
        self.size = self.width * self.height

    def getValue(self, cell: Cell):
        return self.values2D[cell.y][cell.x]

    def setValue(self, cell: Cell, value):
        self.values2D[cell.y][cell.x] = value

    def values(self):
        for cell in self.cells():
            yield self.getValue(cell)

    def cells(self):
        for y in range(self.height):
            for x in range(self.width):
                yield Cell(x, y)

    def isInDomain(self, cell: Cell):
        return cell.x > -1 and cell.y > -1 and cell.x < self.width and cell.y < self.height

    def sideCells(self, cell: Cell):
        x = cell.x
        y = cell.y
        for n in filter(self.isInDomain, [
            Cell(x-1, y),
            Cell(x+1, y),
            Cell(x, y-1),
            Cell(x, y+1),
        ]):
            yield n

    def sideValues(self, cell: Cell):
        for n in self.sideCells(cell):
            yield self.getValue(n)

    def sideCellsAndValues(self, cell: Cell):
        for n in self.sideCells(cell):
            yield CellAndValue(n, self.getValue(n))

    def diagnalCells(self, cell: Cell):
        x = cell.x
        y = cell.y
        for n in filter(self.isInDomain, [
            Cell(x-1, y+1),
            Cell(x+1, y+1),
            Cell(x-1, y-1),
            Cell(x+1, y-1),
        ]):
            yield n

    def diagnalValues(self, cell: Cell):
        for n in self.diagnalCells(cell):
            yield self.getValue(n)

    def diagnalCellsAndValues(self, cell: Cell):
        for n in self.diagnalCells(cell):
            yield CellAndValue(n, self.getValue(n))

    #
    def neighborCells(self, cell: Cell):
        for n in self.sideCells(cell):
            yield n
        for n in self.diagnalCells(cell):
            yield n

    def neighborValues(self, cell: Cell):
        for n in self.neighborCells(cell):
            yield self.getValue(n)

    def neighborCellsAndValues(self, cell: Cell):
        for n in self.neighborCells(cell):
            yield CellAndValue(n, self.getValue(n))


grid = Grid2D([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print("Value at 2,1")
print(grid.getValue(Cell(2, 1)))

print("Cells")
print(tuple(grid.cells()))

print("Values")
print(tuple(grid.values()))

print("Center Side Cells")
print(tuple(grid.neighborValues(Cell(1, 1))))

print("First Side Cells")
print(tuple(grid.neighborValues(Cell(0, 0))))
