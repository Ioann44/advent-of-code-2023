from collections import Counter
import math, re, functools, bisect
from typing import Generator, Any, Iterable, List, Tuple
import tqdm

with open("input.txt", "r") as file_in:
    lines = [line.strip().split() for line in file_in]

grades = list(reversed("AKQT98765432J0"))


def getHandSet(hand: str) -> Tuple[int, Counter[str]]:
    cnt = Counter(hand)
    j_cnt = cnt["J"]
    del cnt["J"]
    return (j_cnt, cnt)


# This is not I want show
def getRank(hand: str) -> int | float:
    total = 0
    for i in range(5, 0, -1):
        total += 14 ** (i - 1) * grades.index(hand[-i])
    j_count, hand_set = getHandSet(hand)
    rank = 0
    if 5 in hand_set.values():
        rank = 6
    elif 4 in hand_set.values():
        rank = 5
        if j_count >= 1:
            rank = 6
    elif 3 in hand_set.values() and 2 in hand_set.values():
        rank = 4
    elif 3 in hand_set.values():
        rank = 3
        if j_count == 1:
            rank = 5
        elif j_count >= 2:
            rank = 6
    elif list(hand_set.values()).count(2) == 2:
        rank = 2
        if j_count == 1:
            rank = 4
        elif j_count == 2:
            rank = 5
        elif j_count >= 3:
            rank = 6
    elif 2 in hand_set.values():
        rank = 1
        if j_count == 1:
            rank = 3
        elif j_count == 2:
            rank = 5
        elif j_count >= 3:
            rank = 6
    else:
        if j_count == 1:
            rank = 1
        elif j_count == 2:
            rank = 3
        elif j_count == 3:
            rank = 5
        elif j_count >= 4:
            rank = 6

    total += 1e8 * rank
    return total


lines = [(line[0], int(line[1]), getRank(line[0])) for line in lines]

lines.sort(key=lambda x: x[2])

res = 0
for i in range(len(lines)):
    res += (i + 1) * lines[i][1]

print(res)
