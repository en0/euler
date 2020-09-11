from euler import elapsed_time, factoral, digit_sum


@elapsed_time()
def solve():
    return digit_sum(factoral(100))


if __name__ == "__main__":
    print("ans:", solve())
