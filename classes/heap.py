import heapq
from collections.abc import Iterable
from typing import TypeVar, Generic

T = TypeVar("T")


class Heap(Generic[T]):
    def __init__(self, items: Iterable[T] = []):
        self.list: Iterable[T] = items.copy()
        heapq.heapify(self.list)

    def size(self):
        return len(self.list)

    def items(self):
        for item in self.list:
            yield item[1]

    def push(self, item: T, val: int):
        heapq.heappush(self.list, (val, item))

    def pop(self) -> T:
        return heapq.heappop(self.list)[1]


# print("Testing heap")

# theHeap = Heap()

# theHeap.push("b", 2)
# theHeap.push("c", 3)
# theHeap.push("a", 1)

# for item in theHeap.items():
#     print(item)
