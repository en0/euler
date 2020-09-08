from datetime import datetime
from math import sqrt
from math import sqrt
from sys import setrecursionlimit


def elapsed_time():
    def decorator(func):
        def wrap(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print("Elapsed Time:", datetime.now() - start)
            return result
        return wrap
    return decorator


def memorize(iter_depth=None):
    if iter_depth:
        setrecursionlimit(iter_depth)
    cache = dict()
    def decorator(func):
        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wrapper
    return decorator


@memorize(10000)
def collatz(n):
    if n == 1:
        return 1
    elif n & 1:
        return collatz(3 * n + 1) + 1
    else:
        return collatz(n // 2) + 1


def prime_factors(n, l=None):
    l = l or []
    if n & 1:
        for i in range(3, int(sqrt(n)) + 1, 2):
            a = n // i
            if n == a * i:
                return prime_factors(a, l + [i])
        return l + [n]
    else:
        return prime_factors(n/2, l + [2])


def fib_seq(limit):
    a, b = 1, 0
    while a < limit:
        b, a = a, b + a
        yield a


def digit_sum(n):
    rt = 0
    for i in str(n):
        rt += int(i)
    return rt


def digital_root(n):
    if n == 0:
        return 0
    else:
        return 1 + ((n - 1) % 9)


def triangular(n):
    n += 1
    return int(n * (n - 1) / 2)


def triangular_root(n):
    return int((sqrt(8 * n + 1) - 1) // 2) + 1


def factors(n):
    i = 1
    ret = []
    while i <= sqrt(n):
        if n % i == 0:
            if n / i == i:
                ret.append(i)
            else:
                ret.append(i)
                ret.append(n // i)
        i = i + 1
    return ret

class Graph():
    def __init__(self, verts):
        self.matrix = []
        for _ in range(verts):
            self.matrix.append([False] * verts)

    def __len__(self):
        return len(self.matrix)
        
    def add_edge(self, a, b):
        self.matrix[a-1][b-1] = True
        self.matrix[b-1][a-1] = True

    def remove_edge(self, a, b):
        self.matrix[a-1][b-1] = False
        self.matrix[b-1][a-1] = False

    def get_connected(self, a):
        ret = []
        for i in range(len(self.matrix)):
            if self.matrix[a-1][i]:
                ret.append(i + 1)
        return ret
