import re

a = open("day1.txt").read()


def ints(s):
    return tuple(map(int, re.findall('[0-9]+', s)))


elves = [ints(x) for x in a.split("\n\n")]
print(elves)

# part 1
print(max(sum(elf) for elf in elves))
