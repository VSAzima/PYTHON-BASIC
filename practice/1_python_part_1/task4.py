"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    inter = []
    i = 0
    total = ''
    word = " # because "
    while i < len(ints):
        power = ints[i] ** 2
        if i == 0:
            inter.append(ints[0])
            part0 = f"[{ints[0]}^2"
            part1 = word + part0 + ","
        else:
            result = power - (ints[i - 1] ** 2 - ints[i - 1])
            inter.append(result)
            if i == len(ints) - 1:
                total += f"{ints[i]}^2 - ({ints[i - 1]}^2 - {ints[i - 1]})]"
            else:
                total += f"{ints[i]}^2 - ({ints[i - 1]}^2 - {ints[i - 1]}), "
        i += 1
    print(inter, part1, total)
