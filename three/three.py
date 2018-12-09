#!/usr/bin/python
import re
import sys
from collections import defaultdict


def parse_claim(claim):
    match = re.search("^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$", claim,
                      re.MULTILINE)
    if not match:
        raise RuntimeError("Bad claim %s" % claim)
    dimensions = list(map(int, match.group(1, 2, 3, 4, 5)))
    return dimensions


def parse_claims(data):
    claims = []
    for line in data:
        claims.append(parse_claim(line))
    return claims


def readFile():
    with open("input.txt") as fp:
        return fp.readlines()


def insert_claim(claim, fabric):
    (claim_number, x, y, width, height) = claim
    for ycoord in range(y, y+height):
        for xcoord in range(x, x+width):
            fabric.setdefault((xcoord, ycoord), []).append(claim_number)


def visualize_fabric(fabric):
    maxxy = max(max(fabric.keys())) + 1
    for y in range(maxxy+1):
        for x in range(maxxy+1):
            points = fabric.get((x, y))
            if not points:
                sys.stdout.write('.')
            elif len(points) == 1:
                sys.stdout.write(str(points[0]))
            else:
                sys.stdout.write('x')
        sys.stdout.write('\n')


def find_overlaps(fabric):
    return len([k for k in fabric if len(fabric.get(k)) > 1])


def find_non_overlapping(fabric, claims):
    overlaps = set()
    for v in fabric.values():
        if len(v) > 1:
            overlaps.update(v)
    for num in claims:
        if num not in overlaps:
            return num


def main():
    fabric = {}
    test1 = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    testclaims = test1.split('\n')
    nums = []
    for line in testclaims:
        claim = parse_claim(line)
        nums.append(claim[0])
        insert_claim(claim, fabric)
    print ("No overlaps: %d" % find_non_overlapping(fabric, nums))
    visualize_fabric(fabric)
    sqinches = find_overlaps(fabric)
    assert sqinches == 4, "square inches should be 4: %s" % sqinches
    fabric = {}
    claims = parse_claims(readFile())
    nums = []
    for claim in claims:
        nums.append(claim[0])
        insert_claim(claim, fabric)
#    visualize_fabric(fabric)
    sqinches = find_overlaps(fabric)
    print("%d overlapping square inches" % sqinches)
    print("No overlaps: %d" % find_non_overlapping(fabric, nums))
    return 0


if __name__ == "__main__":
    exit(main())
