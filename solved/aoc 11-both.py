from collections import Counter, defaultdict
import math, re, functools, bisect
from typing import Dict, Generator, Any, Iterable, List, Tuple
from tqdm import tqdm, trange

with open("input.txt", "r") as file_in:
    lines = [line.strip() for line in file_in]

n = len(lines)
m = len(lines[0])

empty_rows = []
empty_cols = []

for j in trange(m, ncols=80, desc="Compute empty cols"):
    it_empty = True
    for i in range(n):
        if lines[i][j] != ".":
            it_empty = False
    if it_empty:
        empty_cols.append(j)
for i, line in tqdm(enumerate(lines), ncols=80, desc="Compute empty rows"):
    if line.count(".") == m:
        empty_rows.append(i)

e_rows_cnt = 0
e_cols_cnt = 0
MUL = int(1e6) # Expansion, 1 initially (for 1st task)
galaxies: List[Tuple[int, int]] = []
for i, line in tqdm(enumerate(lines), ncols=80, desc="Compute real coordinates"):
    while e_rows_cnt < len(empty_rows) and empty_rows[e_rows_cnt] <= i:
        e_rows_cnt += 1
    e_cols_cnt = 0
    for j, char in enumerate(line):
        while e_cols_cnt < len(empty_cols) and empty_cols[e_cols_cnt] <= j:
            e_cols_cnt += 1
        if char == "#":
            galaxies.append((i + e_rows_cnt * (MUL - 1), j + e_cols_cnt * (MUL - 1)))

res = 0
for i, g1 in tqdm(enumerate(galaxies), ncols=80, desc="Get answer"):
    for g2 in galaxies[i + 1 :]:
        res += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
print(res)
