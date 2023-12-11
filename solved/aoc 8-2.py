from collections import Counter, defaultdict
import math, re, functools, bisect
from typing import Dict, Generator, Any, Iterable, List, Tuple
import tqdm

with open("input.txt", "r") as file_in:
    lines = [line.strip() for line in file_in if line.strip()]

instructions = lines[0]
d_re = re.compile(r"(\w+) = \((\w+), (\w+)\)")
matches: Iterable[re.Match[str]] = (d_re.match(line) for line in lines[1:])  # type: ignore

g: Dict[str, Tuple[str, str]] = dict()
for match in matches:
    g[match.group(1)] = (match.group(2), match.group(3))

a_starts: List[str] = [key for key in g.keys() if key.endswith("A")]
Str_to_tuple = Dict[str, Tuple[int, int]]
z_ends: Str_to_tuple = dict()
cur = a_starts[:]

i = 0
res = 1
while cur:
    if instructions[i] == "L":
        for j, v in enumerate(cur):
            cur[j] = g[v][0]
    else:
        for j, v in enumerate(cur):
            cur[j] = g[v][1]
    for v in cur:
        if v.endswith("Z"):
            z_ends[v] = (i, res)
            cur.remove(v)
    res += 1
    i = (i + 1) % len(instructions)
# as I see, all of them ends in i = 282 (in different times though) (and only once)

cicles: Dict[str, Tuple[str, int, int]] = dict()
for v, end_tuple in z_ends.items():
    cur = v
    i = end_tuple[0]
    shift = 1

    i = (i + 1) % len(instructions)
    while True:
        if instructions[i] == "L":
            cur = g[cur][0]
        else:
            cur = g[cur][1]
        if cur.endswith("Z"):
            cicles[v] = (cur, i, shift)
            break
        shift += 1
        i = (i + 1) % len(instructions)
# And all of them ends in their own vertices, and shifts equal to initial times when they came to them!

# So, only I need with this dataset, is to compute lcm of all the initial times of arriving into this vertex
times = [val[1] for val in z_ends.values()]
print(math.lcm(*times))