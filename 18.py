from euler import elapsed_time, triangular, triangular_root

sample_set = [
    3,
    7,4,
    2,4,6,
    8,5,9,3,
]

problem_set = [
    75,
    95,64,
    17,47,82,
    18,35,87,10,
    20, 4,82,47,65,
    19, 1,23,75, 3,34,
    88, 2,77,73, 7,63,67,
    99,65, 4,28, 6,16,70,92,
    41,41,26,56,83,40,80,70,33,
    41,48,72,33,47,32,37,16,94,29,
    53,71,44,65,25,43,91,52,97,51,14,
    70,11,33,28,77,73,17,78,39,68,17,57,
    91,71,52,38,17,14,91,43,58,50,27,29,48,
    63,66, 4,68,89,53,67,30,73,16,69,87,40,31,
     4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23,
]

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left: "TreeNode" = None
        self.right: "TreeNode" = None

    @property
    def answer(self):
        return max(
            self.value + (self.left.answer if self.left else 0),
            self.value + (self.right.answer if self.right else 0)
        )

    def __repr__(self):
        return f"<TreeNode value={self.value}>"


def parse(raw):
    """Convert an array into a tree.

    The array is interpated as a stack of Triangular numbers such
    that each node is above 2 nodes in the next triangular row

    Example = [
      1,
      2, 3,
      4, 5, 6,
    ]

    The resulting tree from the given example is as follows:

         1
        / \ 
       2   3
      / \ / \ 
     4   5   6
    """
    raw = [TreeNode(v) for v in raw]
    get_node = lambda i: raw[i] if i < len(raw) else None
    for i in range(0, len(raw)):
        root_index = triangular(triangular_root(i) - 1)
        next_index = triangular(triangular_root(i)) + (i - root_index)
        node = get_node(i)
        node.left = get_node(next_index)
        node.right = get_node(next_index + 1)
    return raw[0]


@elapsed_time()
def solve():
    root = parse(problem_set)
    return root.answer


if __name__ == "__main__":
    print("ans:", solve())
