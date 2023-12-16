from collections import Counter, defaultdict
import math, re, functools, bisect
from typing import Dict, Generator, Any, Iterable, List, Tuple, Set
from tqdm import tqdm, trange

with open("input.txt", "r") as file_in:
    data = [[]]
    for line in file_in:
        line = line.strip()
        if line:
            data[-1].append(line)
        else:
            data.append([])

res = 0
symbs = ".#"
MOD = int(1e9 + 7)
PRIME = 17


def get_hash(l: int, r: int, hsh_arr: List[int], reversed=False) -> int:
    if not reversed:
        cur = hsh_arr[r - 1]
        cur -= (hsh_arr[l - 1] if l > 0 else 0) * PRIME ** (r - l)
    else:
        cur = hsh_arr[l]
        cur -= (hsh_arr[r] if r < len(hsh_arr) else 0) * PRIME ** (r - l)
    cur %= MOD
    return cur


for data_set in data:
    n = len(data_set)
    m = len(data_set[0])

    # horizontal
    hsh = [0] * m
    for j in range(m):
        hsh[j] = hsh[j - 1] * PRIME if j > 0 else 0
        hsh[j] += sum(symbs.index(data_set[i][j]) * (1 << i) for i in range(n))
        hsh[j] %= MOD
    # horizontal reversed
    hsh_rev = [0] * m
    for j in range(m - 1, -1, -1):
        hsh_rev[j] = hsh_rev[j + 1] * PRIME if j < m - 1 else 0
        hsh_rev[j] += sum(symbs.index(data_set[i][j]) * (1 << i) for i in range(n))
        hsh_rev[j] %= MOD
    # horizontal check
    for j in range(1, m):
        length = min(j, m - j)
        hsh_left = get_hash(j - length, j, hsh)
        hsh_right = get_hash(j, j + length, hsh_rev, reversed=True)
        if hsh_left == hsh_right:
            res += j

    # horizontal
    hsh = [0] * n
    for i in range(n):
        hsh[i] = hsh[i - 1] * PRIME if i > 0 else 0
        hsh[i] += sum(symbs.index(data_set[i][j]) * (1 << j) for j in range(m))
        hsh[i] %= MOD
    # horizontal reversed
    hsh_rev = [0] * n
    for i in range(n - 1, -1, -1):
        hsh_rev[i] = hsh_rev[i + 1] * PRIME if i < n - 1 else 0
        hsh_rev[i] += sum(symbs.index(data_set[i][j]) * (1 << j) for j in range(m))
        hsh_rev[i] %= MOD
    # horizontal check
    for i in range(1, n):
        length = min(i, n - i)
        hsh_left = get_hash(i - length, i, hsh)
        hsh_right = get_hash(i, i + length, hsh_rev, reversed=True)
        if hsh_left == hsh_right:
            res += 100 * i

print(res)
