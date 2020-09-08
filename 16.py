from euler import elapsed_time, digit_sum


@elapsed_time()
def solve():
    v = 2**1000
    return digit_sum(v)


if __name__ == "__main__":
    print("ans:", solve())
