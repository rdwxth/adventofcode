import re
from collections import defaultdict

def read_input(filename):
    with open(filename) as file:
        return file.read().strip().split('\n\n')

class Function:
    def __init__(self, S):
        lines = S.split('\n')[1:]  # throw away name
        # dst src sz
        self.tuples = [[int(x) for x in line.split()] for line in lines]

    def apply_one(self, x):
        for (dst, src, sz) in self.tuples:
            if src <= x < src + sz:
                return x + dst - src
        return x

    def apply_range(self, R):
        A = []
        for (dest, src, sz) in self.tuples:
            src_end = src + sz
            NR = []
            while R:
                (st, ed) = R.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        return A + R

def main():
    # Read input from "input.txt"
    data = read_input("input.txt")

    seed, *others = data
    seed = [int(x) for x in seed.split(':')[1].split()]

    Fs = [Function(s) for s in others]

    P1 = []
    for x in seed:
        for f in Fs:
            x = f.apply_one(x)
        P1.append(x)
    print(min(P1))

    P2 = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for st, sz in pairs:
        # inclusive on the left, exclusive on the right
        # e.g. [1,3) = [1,2]
        # length of [a,b) = b-a
        # [a,b) + [b,c) = [a,c)
        R = [(st, st + sz)]
        for f in Fs:
            R = f.apply_range(R)
        P2.append(min(R)[0])
    print(min(P2))

if __name__ == "__main__":
    main()
