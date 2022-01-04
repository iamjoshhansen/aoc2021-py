from collections import namedtuple
from run import run

Point = namedtuple("Point", "x y")


class Box:
    def __init__(self, left=0, right=0, bottom=0, top=0):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top
        self.width = right - left
        self.height = top - bottom

    def hasPoint(self, point: Point):
        return point.x > self.left-1 and point.x < self.right+1 and point.y > self.bottom-1 and point.y < self.top+1


class Probe:
    def __init__(self, initialVelocity: Point, initialPosition=Point(0, 0)):
        self.initialVelocity = initialVelocity
        self.initialPosition = initialPosition

    def points(self, maxDepth: int):
        position: dict[str, int] = {
            'x': self.initialPosition.x, 'y': self.initialPosition.y}
        velocity: dict[str, int] = {
            'x': self.initialVelocity.x, 'y': self.initialVelocity.y}
        while position['y'] > maxDepth - 1:
            yield Point(position['x'], position['y'])
            position['x'] += velocity['x']
            position['y'] += velocity['y']
            if velocity['x'] > 0:
                velocity['x'] -= 1
            if velocity['x'] < 0:
                velocity['x'] += 1
            velocity['y'] -= 1


def solve(input: str):
    # target area: x=20..30, y=-10..-5
    [xPart, ys] = input.split(', y=')
    [_, xs] = xPart.split('=')
    xStrings = xs.split('..')
    [left, right] = sorted(map(int, xStrings))

    yStrings = ys.split('..')
    [bottom, top] = sorted(map(int, yStrings))

    box = Box(left=left, right=right, top=top, bottom=bottom)
    origin = Point(0, 0)

    probe = Probe(Point(7, -box.bottom-1), origin)
    positions = tuple(probe.points(box.bottom))

    # print(positions)
    maxHeight = max(p.y for p in positions)
    print(f"Max height: {maxHeight}")

    # Draw it
    # for y in (-i for i in range(-maxHeight, -box.bottom+2)):
    #     row = f'{y}'.rjust(3)
    #     for x in range(box.right + 2):
    #         point = Point(x, y)
    #         if (point == origin):
    #             row += 'S'
    #         elif point in positions:
    #             row += '#'
    #         elif box.hasPoint(point):
    #             row += 'T'
    #         else:
    #             row += '.'
    #     print(row)

    return maxHeight


if __name__ == "__main__":
    run(solve, 17, 1)
