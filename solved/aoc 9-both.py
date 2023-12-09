from collections import Counter, defaultdict
import math, re, functools, bisect
from typing import Dict, Generator, Any, Iterable, List, Tuple
import tqdm
from util import *

with open("input.txt", "r") as file_in:
    lines = [line.strip() for line in file_in]

res = 0
for line in tqdm.tqdm(lines):
    nums = [[int(num) for num in line.split()]]
    last = nums[-1]
    while any(last_i != 0 for last_i in last):
        last = [last[i] - last[i - 1] for i in range(1, len(last))]
        nums.append(last)
    addition = 0
    for lst in reversed(nums):
        # addition = lst[-1] + addition # Part 1
        addition = lst[0] - addition # Part 2
    res += addition
print(res)