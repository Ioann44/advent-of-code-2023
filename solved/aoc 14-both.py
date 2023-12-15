from collections import Counter, defaultdict
import math, re, functools, bisect
from typing import Dict, Generator, Any, Iterable, List, Tuple
from tqdm import tqdm, trange

with open("input.txt", "r") as file_in:
    lines = [line.strip() for line in file_in.readlines()]

res = 0
n = len(lines)
m = len(lines[0])

# part 1
"""
for j in range(m):
    last_avail = 0
    for i, ch in enumerate(lines[i][j] for i in range(n)):
        if ch == "#":
            last_avail = i + 1
        elif ch == "O":
            res += n - last_avail
            last_avail += 1
print(res)
"""

# part 2
lines = [list(line) for line in lines]


def get_hash():
    res = 0
    for line in lines:
        for ch in line:
            res = (res * 3 + ".O#".find(ch)) % 1000000007
    return res


last_seen = dict()

done = 0
need = int(1e9)
while done != need:
    hsh = get_hash()
    if hsh in last_seen and done != last_seen[hsh]:
        cicle_len = done - last_seen[hsh]
        if cicle_len <= need - done:
            done = need - (need - done) % cicle_len
        last_seen[hsh] = done
        continue
    last_seen[hsh] = done

    pass
    # north
    for j in range(m):
        last_avail = 0
        for i, ch in enumerate(lines[i][j] for i in range(n)):
            if ch == "#":
                last_avail = i + 1
            elif ch == "O":
                lines[i][j] = "."
                lines[last_avail][j] = "O"
                last_avail += 1
    pass
    # west
    for i in range(n):
        last_avail = 0
        for j, ch in enumerate(lines[i][j] for j in range(m)):
            if ch == "#":
                last_avail = j + 1
            elif ch == "O":
                lines[i][j] = "."
                lines[i][last_avail] = "O"
                last_avail += 1
    pass
    # south
    for j in range(m):
        last_avail = n - 1
        for i in range(n - 1, -1, -1):
            ch = lines[i][j]
            if ch == "#":
                last_avail = i - 1
            elif ch == "O":
                lines[i][j] = "."
                lines[last_avail][j] = "O"
                last_avail -= 1
    pass
    # east
    for i in range(n):
        last_avail = m - 1
        for j in range(m - 1, -1, -1):
            ch = lines[i][j]
            if ch == "#":
                last_avail = j - 1
            elif ch == "O":
                lines[i][j] = "."
                lines[i][last_avail] = "O"
                last_avail -= 1
    done += 1

res = 0
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch == "O":
            res += n - i
print(res)
