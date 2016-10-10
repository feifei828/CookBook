import itertools
from itertools import dropwhile
from itertools import islice
from itertools import permutations
from itertools import combinations
from itertools import chain
from collections import Iterable
import heapq

items = [1, 2, 3]
it = iter(items)
next(it)  # 1
next(it)  # 2
next(it)  #3
# next(it)
# StopIteration


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        # 深度优先搜索
        yield self
        for c in self:
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_children(child1)
    root.add_children(child2)
    for ch in root:
        print(ch)  # Node(1) Node(2)
    child1.add_children(Node(3))
    child1.add_children(Node(4))
    child2.add_children(Node(5))
    child2.add_children(Node(6))
    for i in root.depth_first():
        print(i)


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    # 0,0.5,1.0,1.5,2.0,2.5,3.0,3.5
    n

list(frange(0, 4, 0.5))  # [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]


def countdown(n):
    print('start', n)
    while n > 0:
        yield n
        n -= 1
    print('Down!')

c = countdown(3)
list(c)  # start 3 Down! [3, 2, 1]
# next(c)
# start 3 3  2  1  Down!

# 反向迭代
a = [1, 2, 3, 4]
for i in reversed(a):
    i  # 4,3,2,1


def count(n):
    while True:
        yield n
        n += 1

c = count(0)
# 迭代器生成器
for x in itertools.islice(c, 10, 20):
    x

for i in dropwhile(lambda i: i < 2, a):
    i  # 2, 3, 4

for i in islice(a, 2, None):
    i  # 3, 4

for i in permutations(a):
    # 元素之间顺序打乱成所有可能的情况
    i

for i in permutations(a, 2):
    # 长度选择
    i

for i in combinations(a, 4):
    i  # [1, 2, 3, 4]

for idx, val in enumerate(a):
    idx, val

b = [5, 6, 7]
for i in zip(a, b):
    i  # (1, 5) (2, 6) (3, 7)

c = [9, 10, 11]
for i in zip(a,b,c):
    i

for i in chain(b,c):
    i  # 5 6 7 9 10 11


# 扁平化处理嵌套序列
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
list(flatten(items))  # [1, 2, 3, 4, 5, 6, 7, 8]

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
for i in heapq.merge(a, b):
    i  # 1, 2, 3, 4, 5, 6, 7, 8

