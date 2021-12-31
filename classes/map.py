from collections import namedtuple
from typing import Dict, TypeVar, Generic

T = TypeVar("T")


class Map(Generic[T]):
    def __init__(self, identifier):
        self.identifier = identifier
        self.items: Dict[str, T] = {}

    def add(self, item: T):
        id = self.identifier(item)
        self.items[id] = item

    def get(self, item: T) -> T:
        id = self.identifier(item)
        return self.items.get(id)

    def getFromId(self, id: str) -> T:
        return self.items.get(id)

    def has(self, item: T) -> bool:
        id = self.identifier(item)
        return id in self.items


Point = namedtuple("Point", "x y z")


def pointIdentifier(point: Point) -> str:
    return f"{point.x},{point.y},{point.z}"


# m = Map[Point](pointIdentifier)

# a = Point(1, 2, 3)
# b = Point(4, 5, 6)
# c = Point(7, 8, 9)

# m.add(a)
# m.add(b)

# print(m.get(a))
# print(m.get(b))
# print(m.get(c))
