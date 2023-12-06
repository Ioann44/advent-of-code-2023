import math, re, functools, bisect
from typing import Generator, Any, Iterable, List
import tqdm
from util import *

with open("input.txt", "r") as file_in:
    lines = [line.strip() for line in file_in if line.strip()]

total_time, best_dist = (int("".join(line[11:].split())) for line in lines)

res = 0

for hold in tqdm.trange(total_time + 1):
    dist = hold * (total_time - hold)
    if dist > best_dist:
        res += 1

print(res)
