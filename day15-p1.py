from classes.pathfinder import Pathfinder
from run import run
from utils.inputTo2dIntArray import inputTo2dIntArray
from classes.grid2d import Grid2D


def solve(input: str):
    values = inputTo2dIntArray(input)
    grid = Grid2D(values)
    pathfinder = Pathfinder(grid)

    return 42


if __name__ == '__main__':
    run(solve, 15, 1)
