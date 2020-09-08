from euler import elapsed_time, fib_seq


@elapsed_time()
def solve():
    return sum(filter(lambda x: x & 1 == 0, fib_seq(4000000)))


if __name__ == "__main__":
    print("ans:", solve())
