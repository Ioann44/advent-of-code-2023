from collections import Counter, defaultdict
import math, re, functools, bisect
from typing import Dict, Generator, Any, Iterable, List, Tuple
from tqdm import tqdm, trange

reg = re.compile(r"^([?.#]+) ([0-9,]+)\s?$")
with open("input.txt", "r") as file_in:
    lines = [
        [match.group(1), list(map(int, match.group(2).split(",")))]
        for match in (re.match(reg, line) for line in file_in)
        if match
    ]

res = 0
for row, segs in tqdm(lines):
    # part 2 addition on next 2 lines
    row = "?".join(row for _ in range(5))
    segs = segs * 5
    
    n = len(row) + 1
    m = len(segs) + 1
    # 21 * 21 * 7 in worst case (x 125 for part 2)
    dp = [[[0] * m for j in range(n)] for i in range(n)]
    dp[0][0][0] = 1

    for i, ch in enumerate(row):
        for j in range(n):
            for k in range(m):
                cur = dp[i][j][k]
                if cur == 0:
                    continue
                if ch == "#":
                    if j < n - 1:
                        dp[i + 1][j + 1][k] += cur
                else:  # ch == "." or ch == "?"
                    if j == 0:
                        dp[i + 1][0][k] += cur
                    elif k < m - 1 and j == segs[k]:
                        dp[i + 1][0][k + 1] += cur
                if ch == "?":
                    if j < n - 1:
                        dp[i + 1][j + 1][k] += cur
    cur_suppl = dp[-1][0][-1]
    cur_suppl += dp[-1][segs[-1]][-2]
    res += cur_suppl

print(res)
