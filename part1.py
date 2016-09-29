import heapq
from audioop import avg
from collections import deque, defaultdict, OrderedDict
from collections import Counter, namedtuple
from itertools import compress

p = (4, 5)
x, y = p

data = ['ACME', 50, 90.1, (2012, 12, 21)]
name, shares, price, date = data

name, new_shares, new_price, (year, month, day) = data

_, last_shares, last_price, _ = data


s = 'HELLO'
a, b, c, d, e = s


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)  # [2, 3, 4]
q.popleft()  # [3, 4]
q.pop()  # [3]
q.appendleft(5)  # [5, 3]

nums = [1, 4, 5, -6, 7]
heapq.nlargest(2, nums)  # [5, 7]
heapq.nsmallest(2, nums)  # [-6, 1]

portfolio = [
    {'name': 'IBM', 'share': 100, 'price': 30},
    {'name': 'FB', 'share': 20, 'price': 20}
]
# q = {'name': 'FB', 'share': 20, 'price': 20}
q = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])


# use heapq to realize priority
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grop'), 1)
q.pop()
# Item('bar')  Item('spam') Item('foo') Item('grop')


d = defaultdict(list)
d['a'].append(1)

d = {}
d.setdefault('a', []).append(1)

# ordering by add but slow twice than normal dict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2


prices = {
    'A': 12,
    'B': 34,
    'C': 8,
}

# zip() only use once
min_price = min(zip(prices.values(), prices.keys()))  # {8: 'C'}
max_price = max(zip(prices.values(), prices.keys()))  # {34: 'B'}
prices_sorted = sorted(zip(prices.values(), prices.keys()))
min(prices, key=lambda k: prices[k])  # C
min_value = prices[min(prices, key=lambda k: prices[k])]


a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'w': 10,
    'x': 11,
    'y': 2,
}

# a.values() & a.values() is error
a.keys() & b.keys()  # {'x', 'y'}
a.keys() - b.keys()
a.items() & b.items()  # { ('y', 2)}


# use set(a) delete repeated value
# delete repeated value by ordering
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

items = [0, 1, 2, 3, 4]
a = slice(2, 4)
items[a]  # [2, 3]
items[a] = [10, 11]  # [0, 1, 10, 11, 4]

words = ['1', '1', '1', '2', '2', '3']
words_count = Counter(words)
top_two = words_count.most_common(2)  # [('1', 3),('2', 2)]
words_count['1']  # 3

val = [1, 4, -5, 10, -7, 2, 5]

l = [n for n in val if n > 0]


def gt_zero(n):
    if n > 0:
        return True
    else:
        return False

# 1, 4, 10, 2
l = list(filter(gt_zero, val))

list(compress(words, [gt_zero(n) for n in val]))

s = namedtuple('s', ['a', 'b'])
sub = s('x', 'y')  # s(a='x', b='y')

sub.a  # x
sub.b  # y

# cannot use sub.a = 'z'
sub = sub._replace(a='z')  # s(a='z', b='y')

a = {
    'x': 1,
    'z': 3,
}

b = {
    'y': 2,
    'z': 4,
}

merged = dict(b)
merged.update(a) # merge = {'y': 2, 'x': 1, 'z': 3}
