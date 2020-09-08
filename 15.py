from euler import elapsed_time, Graph
from collections import deque


def make_lattice(s):
    """Create a lattice with s**2 verticies

    The lattice is always a square and s indicates how
    wide and tall the square is. The lattice is stored
    as a graph with edges connected along each horizontal
    and vertical axies.


    Example: make_lattice(3)

        O--O--O
        |  |  |
        O--O--O
        |  |  |
        O--O--O
    """
    n = s*s
    g = Graph(n)

    for v in range(n):
        if v % s == 0:
            continue
        g.add_edge(v, v+1)
        if v > s*s-s:
            continue
        g.add_edge(v, v+s)
        g.add_edge(v+1, v+s+1)
    return 1, g, n


def propagate(source, targets, vals):
    """Propagate the value.

    Propagate the value in `vals` pointed to by `source`
    by add the value to each target in `targets`. If a target
    does not exist in `vals`, it is initialized to zero
    before the value is added.
    """
    v = vals[source]
    for t in targets:
        vals.setdefault(t, 0)
        vals[t] += v


@elapsed_time()
def solve():
    """Solve the problem.

    Find all possible paths from the first to the last
    vertex in a 21x21 lattice.
    """

    s, g, e = make_lattice(21)
    stack = deque([[e]])
    vals = {s: 1}
    max_n = 0

    while stack:
        max_n = max(max_n, len(stack))
        n, *p = stack.pop()
        for c in g.get_connected(n):
            if c > n:
                continue
            if c in vals:
                propagate(c, [n] + p, vals)
            else:
                stack.append([c, n] + p)
    return vals[e]


if __name__ == "__main__":
    print("ans:", solve())
