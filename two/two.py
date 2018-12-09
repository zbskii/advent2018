#!/usr/bin/python
from collections import Counter

def readFile():
    with open("input.txt") as fp:
        return fp.readlines()


def calcChecksumOld(ids):
    count3total = 0
    count2total = 0
    for i in ids:
        count2 = 0
        count3 = 0
        x = sorted(i.strip())
        while x:
            if len(x) == 1:
                x.pop()
                continue
            if len(x) == 2:
                if x[0] == x[1]:
                    count2 += 1
                x.pop(0)
                x.pop(0)
                continue
            if x[0] == x[1] == x[2]:
                count3 = 1
                x.pop(0)
                x.pop(0)
                x.pop(0)
                continue
            if x[0] == x[1]:
                count2 = 1
                x.pop(0)
                x.pop(0)
                continue
            x.pop(0)
        count2total += count2
        count3total += count3


    return (count2total, count3total)


def calcChecksum(ids):
    twoCounts = 0
    threeCounts = 0
    for i in ids:
        counts = [x for x in Counter(i).values() if (x == 2 or x ==3)]
        if 2 in counts:
            twoCounts += 1
        if 3 in counts:
            threeCounts += 1
    return twoCounts, threeCounts


def calcDistance(word1, word2):
    distance = [t for t in zip(word1,word2) if t[0] != t[1]]
    return len(distance)

def find_smallest_diff(rids):
    diffs = {}
    ids = [l.strip() for l in rids]
    for b in ids:
        for c in ids:
            if b == c:
                continue
            distance = calcDistance(b, c)
            diffs[distance] = [b, c]
    smallest = min(diffs.keys())
    return sorted(diffs[smallest])

def subtract_letters(word1, word2):
    return ''.join([t[0] for t in zip(word1, word2) if t[0] == t[1]])


def main():
    # assert calcChecksum(["abcdef"]) == (0, 0), calcChecksum(["abcdef"])
    # assert calcChecksum(["bababc"]) == (1, 1), calcChecksum(["bababc"])
    # assert calcChecksum(["abbcde"]) == (1, 0), calcChecksum(["abbcde"])
    # assert calcChecksum(["abcccd"]) == (0, 1), calcChecksum(["abcccd"])
    # assert calcChecksum(["abcdee"]) == (1, 0), calcChecksum(["abcdee"])
    # assert calcChecksum(["ababab"]) == (0, 1), calcChecksum(["ababab"])
    # twos, threes = calcChecksum(ids)
    # return twos * threes
    test1 = ["fghij", "fguij"]
    test2 = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz""".split("\n")
    smallest = find_smallest_diff(test1)
    assert smallest == test1 , "%s != %s" % (test1, smallest)
    smallest2 = find_smallest_diff(test2)
    assert smallest2 == test1, "%s != %s" % (smallest2, test1)
    ids = readFile()
    smallest_a = find_smallest_diff(ids)
    print smallest_a
    print(subtract_letters(smallest_a[0], smallest_a[1]))
    return 0


if __name__ == "__main__":
    exit(main())
