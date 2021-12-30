import heapq


class Heap:
    def __init__(self, items=[]):
        self.list = items.copy()
        heapq.heapify(self.list)

    def items(self):
        for item in self.list:
            yield item[1]

    def push(self, item, val: int):
        heapq.heappush(self.list, (val, item))

    def pop(self):
        return heapq.heappop(self.list)


# print("Testing heap")

# theHeap = Heap()

# theHeap.push('b', 2)
# theHeap.push('c', 3)
# theHeap.push('a', 1)

# for item in theHeap.items():
#     print(item)
