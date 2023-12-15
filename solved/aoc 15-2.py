from collections import Counter, defaultdict
import math, re, functools, bisect
from typing import Dict, Generator, Any, Iterable, List, Tuple
from tqdm import tqdm, trange

with open("input.txt", "r") as file_in:
    lines = [re.split(r"[-=]", line) for line in file_in.readline().split(",")]


@functools.cache
def get_hash(s):
    hsh = 0
    for ch in label:
        hsh = (hsh + ord(ch)) * 17 % 256
    return hsh


ind_by_label: Dict[str, int] = dict()
boxes: List[List[int]] = [[] for _ in range(256)]
for data_set in lines:
    label = data_set[0]
    box_i = get_hash(label)
    if data_set[1]:  # label=foc
        foc = int(data_set[1])
        if label in ind_by_label:
            boxes[box_i][ind_by_label[label]] = foc
        else:
            ind_by_label[label] = len(boxes[box_i])
            boxes[box_i].append(foc)
    else:  # label-
        if label in ind_by_label:
            boxes[box_i][ind_by_label[label]] = 0
            del ind_by_label[label]

boxes = [[foc for foc in box if foc] for box in boxes]
res = 0
for i, box in enumerate(boxes, 1):
    for j, foc in enumerate(box, 1):
        res += i * j * foc  # type: ignore
print(res)
