from euler import elapsed_time


def compute_name_score(name, offset):
    ref = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum([ref.index(c) for c in name]) * (offset+1)


def load_file(path):
    with open(path) as p:
        raw = p.read()
        return sorted([r.strip('"') for r in raw.split(',')])


@elapsed_time()
def solve():
    path = 'assets/p022_names.txt'
    return sum([compute_name_score(n, i) for i, n in enumerate(load_file(path))])


if __name__ == "__main__":
    print("ans:", solve())
