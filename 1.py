from functools import reduce
from euler import elapsed_time


@elapsed_time()
def solve():
    multi = lambda x, l: {_ for _ in range(0, l, x)}
    all_multi = lambda l, s: reduce(lambda a, b: a | multi(b, l), s, set())
    sum_all_multi = lambda l, s: sum(all_multi(l, s))
    return sum_all_multi(1000, [3, 5])


if __name__ == "__main__":
    print("ans:", solve())
