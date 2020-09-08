from euler import triangular, factors, elapsed_time


@elapsed_time()
def solve():
    i = 1
    while True:
        t = triangular(i)
        l = factors(t)
        if len(l) > 500:
            return t
        i += 1


if __name__ == "__main__":
    print("ans:", solve())
