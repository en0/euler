from euler import elapsed_time


class WordNames():

    ones = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    tens = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }

    names = {
        0: "",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    def __init__(self):
        self._names = dict(WordNames.names)
        self._ones = dict(WordNames.ones)
        self._tens = dict(WordNames.tens)
        for i in range(1, 10):
            self._names[i] = self._ones[i]

        for i in range(20, 100):
            o = self._ones[i%10]
            self._names[i] = self._tens[i//10] + (("-" + o) if o else "")

        for i in range(100,1000):
            o = self._names[i%100]
            self._names[i] = self._ones[i//100] + " hundred" + (" and " + o if o else "")

        self._names[1000] = "one thousand"

    def __getitem__(self, i):
        return self._names[i]


@elapsed_time()
def solve():
    rt = 0
    names = WordNames()
    for i in range(1000):
        n = names[i + 1]
        print(n)
        rt += len([_ for _ in n if _ in "abcdefghijklmnopqrstuvwxyz"])
    return rt


if __name__ == "__main__":
    print("ans:", solve())
