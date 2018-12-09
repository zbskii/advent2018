#!/usr/bin/python

def readFile():
    with open("freq.txt") as fp:
        return fp.readlines()

def calcFreq(freqs):
    seen = {0: True}
    total = 0
    while True:
        for f in freqs:
            btotal = total
            total += int(f)
            if total in seen:
                return total
            seen[total] = True


def main():
    freq = readFile()
    print calcFreq(freq)

if __name__ == "__main__":
    exit(main())
