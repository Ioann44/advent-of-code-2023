import math, re, functools, bisect
from typing import Generator, Any, Iterable, List

with open("input.txt", "r") as file_in:
    lines = [line.strip() for line in file_in if line.strip()]

data = []


class Bind:
    src = 0
    dest = 0
    size = 0

    def __init__(self, *dataIn: int) -> None:
        self.src, self.dest, self.size = dataIn

    def __lt__(self, other):
        return self.src < other.src


class Seg:
    start = 0
    size = 0

    def __init__(self, *dataIn: int) -> None:
        self.start, self.size = dataIn

    def __lt__(self, other):
        return self.start < other.start


def unite_segments(segments: List[Seg]):
    segments.sort()
    new_segments = [segments[0]]
    for i in range(1, len(segments)):
        si = segments[i]
        last_new = new_segments[-1]
        if last_new.start + last_new.size >= si.start:
            new_segments[-1].size = si.start + si.size - last_new.start
        else:
            new_segments.append(si)
    return new_segments


seeds_in_data = [int(num) for num in lines[0][7:].split()]
segments = [Seg(*chunk) for chunk in zip(seeds_in_data[::2], seeds_in_data[1::2])]
segments = unite_segments(segments)

for line in lines[1:]:
    if line.endswith("map:"):
        data.append([])
    else:
        dst, src, sz = [int(num) for num in line.split()]
        data[-1].append(Bind(src, dst, sz))

for di in data:
    di.sort()

for di in data:
    new_segments = []
    j = 0
    dij: Bind = di[j]
    i = 0
    while i < len(segments):
        seg = segments[i]

        if seg.size == 0:
            i += 1
            continue

        while dij and dij.src + dij.size <= seg.start:
            j += 1
            dij = None if j == len(di) else di[j]  # type: ignore

        if dij is None:
            new_segments.append(seg)
            i += 1
        elif dij.src > seg.start:
            new_segments.append(Seg(seg.start, min(dij.src - seg.start, seg.size)))
            segments[i].size -= new_segments[-1].size
            segments[i].start += new_segments[-1].size
        else:
            new_segments.append(Seg(seg.start, min(seg.size, dij.src + dij.size - seg.start)))
            segments[i].start = new_segments[-1].start + new_segments[-1].size
            segments[i].size -= new_segments[-1].size
            new_segments[-1].start += dij.dest - dij.src

    segments = unite_segments(new_segments)

print(segments[0].start)
