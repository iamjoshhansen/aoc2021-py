from collections import namedtuple
from typing import Dict, Generic, Iterable, Tuple, TypeVar
from classes.heap import Heap
from classes.grid2d import Cell, CellAndValue, Grid2D
from classes.map import Map
from run import clr

Explorer = namedtuple("Explorer", "cell totalRisk origin")
T = TypeVar("T")


def cellId(cell: Cell) -> str:
    return f"{cell.x},{cell.y}"


def nextStepFilter(
    source: Explorer,
    next: CellAndValue,
    signs: Map[Explorer],
    grid: Grid2D,
    start: Cell,
) -> bool:
    if next.cell == start:
        return False
    existing = signs.get(next)
    if existing == None:
        return True
    addedRisk = grid.getValue(next.cell)
    newTotalRisk = source.totalRisk + addedRisk
    return newTotalRisk < existing.totalRisk


def totalRiskFromCell(cell: Cell, signs) -> str:
    sign = signs.getFromId(cellId(cell))
    if sign == None:
        return "-"
    return f"{sign.totalRisk}"


class Pathfinder(Generic[T]):
    def __init__(self, grid: Grid2D[T]):
        self.grid = grid

    def getPath(self, start: Cell, end: Cell) -> Tuple[Cell]:
        # Setup
        explorers: Heap[Explorer] = Heap[Explorer]()
        signs = Map(lambda explorer: cellId(explorer.cell))
        firstExplorer = Explorer(start, 0, None)
        explorers.push(firstExplorer, 0)

        # Send out explorers (discover all risks)
        foundTarget = False
        while explorers.size() > 0 and foundTarget == False:
            bestExplorer: Explorer = explorers.pop()
            # print(f"bestExplorer {bestExplorer}")
            neighbors = self.grid.sideCellsAndValues(bestExplorer.cell)
            nextSteps = filter(
                lambda cv: nextStepFilter(bestExplorer, cv, signs, self.grid, start),
                neighbors,
            )
            for cv in nextSteps:
                nRisk = bestExplorer.totalRisk + cv.value
                newExplorer = Explorer(cv.cell, nRisk, bestExplorer.cell)
                signs.add(newExplorer)
                explorers.push(newExplorer, newExplorer.totalRisk)
                if newExplorer.cell == end:
                    foundTarget = True

        # print("Costs")
        # for row in self.grid.cells2D():
        #     print(
        #         " ".join(
        #             map(
        #                 lambda cell: totalRiskFromCell(cell, signs).rjust(2),
        #                 row,
        #             )
        #         )
        #     )

        # print("Path")
        path: Iterable[Cell] = []
        cursor = end
        while cursor != None:
            path.append(cursor)
            sign = signs.getFromId(cellId(cursor))
            if sign != None:
                cursor = sign.origin
            else:
                cursor = None

        path.pop()
        path.reverse()

        return tuple(path)
