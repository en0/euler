from euler import collatz, elapsed_time

@elapsed_time()
def solve():
    longest = 0
    ans = 0

    for i in range(1000000, 13, -1):
        l = collatz(i)
        if l > longest:
            longest = l
            ans = i
            print(i)

    return ans


if __name__ == "__main__":
    print("ans:", solve())
