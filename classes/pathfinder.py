from classes.heap import Heap
from grid2d import Cell, Grid2D


class PathExplorer:
    def __init__(self, grid: Grid2D, cell: Cell, totalRisk=0, origin: Cell = None):
        self.grid = grid
        self.cell = cell
        self.totalRisk = totalRisk
        self.origin = origin


class Pathfinder:
    def __init__(self, grid: Grid2D):
        self.grid = grid

    def getPath(self, start: Cell, end: Cell):
        explorers = Heap()
        return (Cell(0, 0), Cell(0, 1))
