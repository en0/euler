from euler import elapsed_time, prime_factors
from math import sqrt


@elapsed_time()
def solve():
    return max(prime_factors(600851475143))


if __name__ == "__main__":
    print("ans:", solve())
