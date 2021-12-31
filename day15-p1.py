from classes.pathfinder import Pathfinder
from run import clr, run
from utils.inputTo2dIntArray import inputTo2dIntArray
from classes.grid2d import Cell, Grid2D


def solve(input: str):
    values = inputTo2dIntArray(input)
    grid = Grid2D(values)

    # for row in grid.values2D:
    #     print(" ".join(map(str, row)))

    pathfinder = Pathfinder(grid)

    # print()

    path = pathfinder.getPath(Cell(0, 0), Cell(grid.width - 1, grid.height - 1))
    # for row in grid.cells2D():
    #     print(
    #         " ".join(
    #             map(
    #                 lambda cell: (
    #                     f"{clr.DIM}{grid.getValue(cell)}{clr.RESET}",
    #                     f"{clr.OKBLUE}{grid.getValue(cell)}{clr.RESET}",
    #                 )[cell in path],
    #                 row,
    #             )
    #         )
    #     )

    # print()

    pathRisks = tuple(map(lambda cell: grid.getValue(cell), path))
    # print("risks:")
    # print(pathRisks)

    pathRisk = sum(pathRisks)
    return pathRisk


if __name__ == "__main__":
    run(solve, 15, 1)
