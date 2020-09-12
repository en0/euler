from euler import elapsed_time, factors, memorize
from functools import lru_cache


@memorize()
def D(n):
    # assumption: factors() returns 1 and 2 in the first
    # 2 positions of the result set.
    return sum(factors(n)[2:]) + 1


def is_amicable(n):
    a = D(n)
    return n == D(a) and n != a


@elapsed_time()
def solve():
    return sum({i for i in range(1, 10000) if is_amicable(i)})


if __name__ == "__main__":
    print("ans:", solve())
