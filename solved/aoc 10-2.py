from collections import Counter, defaultdict
import math, re, functools, bisect
from typing import Dict, Generator, Any, Iterable, List, Tuple
import tqdm

prev = [30, 119]
cur = [30, 120]
# prev = [1, 1]
# cur = [1, 2]
nxt = [0, 0]
cnt = 1


with open("input.txt", "r") as file_in:
    lines = [line.strip() for line in file_in]


cur_ch = lines[cur[0]][cur[1]]

tile_in_loop = set((tuple(prev), tuple(cur)))

while cur_ch != "S":
    nxt = cur[:]
    match cur_ch:
        case "|":
            if prev[0] == cur[0] - 1:
                nxt[0] = cur[0] + 1
            else:
                nxt[0] = cur[0] - 1
        case "-":
            if prev[1] == cur[1] - 1:
                nxt[1] = cur[1] + 1
            else:
                nxt[1] = cur[1] - 1
        case "L":
            if prev[0] == cur[0] - 1:
                nxt[1] += 1
            else:
                nxt[0] -= 1
        case "J":
            if prev[1] == cur[1] - 1:
                nxt[0] -= 1
            else:
                nxt[1] -= 1
        case "7":
            if prev[1] == cur[1] - 1:
                nxt[0] += 1
            else:
                nxt[1] -= 1
        case "F":
            if prev[0] == cur[0] + 1:
                nxt[1] += 1
            else:
                nxt[0] += 1
    prev, cur = cur, nxt
    tile_in_loop.add(tuple(cur))
    cur_ch = lines[cur[0]][cur[1]]
    cnt += 1
# print((cnt + 1) // 2)

res = 0

for k in tqdm.trange(-len(lines[0]), len(lines)):
    i = k
    j = 0
    if i < 0:
        i = 0
        j = abs(k)
    is_in = False
    while i < len(lines) and j < len(lines[0]):
        if (i, j) in tile_in_loop:
            if lines[i][j] not in ["7", "L"]:
                is_in = not is_in
        elif is_in:
            res += 1
        i += 1
        j += 1

print(res)
