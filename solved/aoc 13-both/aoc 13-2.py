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
# PRIME = 31


def get_hash(l: int, r: int, hsh_arr: List[int], reversed=False) -> int:
    if not reversed:
        cur = hsh_arr[r - 1]
        cur -= (hsh_arr[l - 1] if l > 0 else 0) * PRIME ** (r - l)
    else:
        cur = hsh_arr[l]
        cur -= (hsh_arr[r] if r < len(hsh_arr) else 0) * PRIME ** (r - l)
    cur %= MOD
    return cur


def check_hashes_are_equal(i: int, hsh: List[int], hsh_rev: List[int]) -> bool:
    n = len(hsh)
    length = min(i, n - i)
    hsh_left = get_hash(i - length, i, hsh)
    hsh_right = get_hash(i, i + length, hsh_rev, reversed=True)
    return hsh_left == hsh_right


for data_set in tqdm(data):
    n = len(data_set)
    m = len(data_set[0])

    # vertical
    vertical_symmetry = 0
    hsh_vert = [0] * m
    for j in range(m):
        hsh_vert[j] = hsh_vert[j - 1] * PRIME if j > 0 else 0
        hsh_vert[j] += sum(symbs.index(data_set[i][j]) * (1 << i) for i in range(n))
        hsh_vert[j] %= MOD
    # vertical reversed
    hsh_rev_vert = [0] * m
    for j in range(m - 1, -1, -1):
        hsh_rev_vert[j] = hsh_rev_vert[j + 1] * PRIME if j < m - 1 else 0
        hsh_rev_vert[j] += sum(symbs.index(data_set[i][j]) * (1 << i) for i in range(n))
        hsh_rev_vert[j] %= MOD
    # vertical check
    for j in range(1, m):
        if check_hashes_are_equal(j, hsh_vert, hsh_rev_vert):
            vertical_symmetry = j
            break

    # horizontal
    horizontal_symmetry = 0
    hsh_hor = [0] * n
    for i in range(n):
        hsh_hor[i] = hsh_hor[i - 1] * PRIME if i > 0 else 0
        hsh_hor[i] += sum(symbs.index(data_set[i][j]) * (1 << j) for j in range(m))
        hsh_hor[i] %= MOD
    # horizontal reversed
    hsh_rev_hor = [0] * n
    for i in range(n - 1, -1, -1):
        hsh_rev_hor[i] = hsh_rev_hor[i + 1] * PRIME if i < n - 1 else 0
        hsh_rev_hor[i] += sum(symbs.index(data_set[i][j]) * (1 << j) for j in range(m))
        hsh_rev_hor[i] %= MOD
    # horizontal check
    for i in range(1, n):
        if check_hashes_are_equal(i, hsh_hor, hsh_rev_hor):
            horizontal_symmetry = i
            break

    done = False
    for i in range(n):
        if done:
            break
        for j in range(m):
            if done:
                break
            hsh_hor_copy = hsh_hor[:]
            hsh_rev_hor_copy = hsh_rev_hor[:]
            hsh_vert_copy = hsh_vert[:]
            hsh_rev_vert_copy = hsh_rev_vert[:]

            old_ch = data_set[i][j]
            mul = 1 if old_ch == "." else -1
            for j2 in range(m):
                if j2 >= j:
                    hsh_vert_copy[j2] += mul * (1 << i) * PRIME ** (j2 - j)
                    hsh_vert_copy[j2] %= MOD
                if j2 <= j:
                    hsh_rev_vert_copy[j2] += mul * (1 << i) * PRIME ** (j - j2)
                    hsh_rev_vert_copy[j2] %= MOD
            for i2 in range(n):
                if i2 >= i:
                    hsh_hor_copy[i2] += mul * (1 << j) * PRIME ** (i2 - i)
                    hsh_hor_copy[i2] %= MOD
                if i2 <= i:
                    hsh_rev_hor_copy[i2] += mul * (1 << j) * PRIME ** (i - i2)
                    hsh_rev_hor_copy[i2] %= MOD

            for j3 in range(1, m):
                if check_hashes_are_equal(j3, hsh_vert_copy, hsh_rev_vert_copy):
                    if vertical_symmetry != j3:
                        res += j3
                        done = True
                        break
            for i3 in range(1, n):
                if check_hashes_are_equal(i3, hsh_hor_copy, hsh_rev_hor_copy):
                    if horizontal_symmetry != i3:
                        res += 100 * i3
                        done = True
                        break

print(res)
