from collections import Counter, defaultdict
import math, re, functools, bisect
from typing import Dict, Generator, Any, Iterable, List, Tuple, Set
from tqdm import tqdm, trange

with open("input.txt", "r") as file_in:
    lines = [line.strip() for line in file_in.readlines()]

n = len(lines)
m = len(lines[0])

res = 0

# for k in trange(2 * m, 2 * m + 1): # use this line for task 1
for k in trange(n * 2 + m * 2):
    initI, initJ, initDirection = 0, 0, 0
    if k < m:
        initJ = k
        initDirection = 2
    elif m <= k < 2 * m:
        initI = n - 1
        initJ = k - m
        initDirection = 0
    else:
        k -= 2 * m
        if k < n:
            initI = k
            initDirection = 1
        elif n <= k < 2 * n:
            initJ = m - 1
            initI = k - n

    queue: List[Tuple[int, int, int]] = [(initI, initJ, initDirection)]

    used: Set[Tuple[int, int, int]] = set()  # i, j, direction (0 up, 1 right, 2 down, 3 left)
    que_ind = 0
    while que_ind < len(queue):
        i, j, direction = queue[que_ind]
        if queue[que_ind] not in used and 0 <= i < n and 0 <= j < m:
            used.add(queue[que_ind])

            ch = lines[i][j]
            if ch == "\\":
                if direction == 0:
                    queue.append((i, j - 1, 3))
                elif direction == 1:
                    queue.append((i + 1, j, 2))
                elif direction == 2:
                    queue.append((i, j + 1, 1))
                else:
                    queue.append((i - 1, j, 0))

            elif ch == "/":
                if direction == 0:
                    queue.append((i, j + 1, 1))
                elif direction == 1:
                    queue.append((i - 1, j, 0))
                elif direction == 2:
                    queue.append((i, j - 1, 3))
                else:
                    queue.append((i + 1, j, 2))

            elif ch == "-" and (direction & 1) == 0:
                queue.extend(((i, j - 1, 3), (i, j + 1, 1)))

            elif ch == "|" and (direction & 1):
                queue.extend(((i - 1, j, 0), (i + 1, j, 2)))

            else:
                if direction & 1:
                    j += 1 - 2 * int(direction == 3)
                else:
                    i += 1 - 2 * int(direction == 0)
                queue.append((i, j, direction))

        que_ind += 1

    used_shrinked = {(i, j) for i, j, _ in used}
    res = max(res, len(used_shrinked))

print(res)