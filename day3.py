import os
import re

def part_2(input) -> int:
    mult_total = 0
    do = True
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    for line in input:
        matches = re.findall(pattern, line)
        for m in matches:
            if m == "do()":
                do = True
            elif m == "don't()":
                do = False
            else:
                if do:
                    numbers =  m[3:].strip("()").split(",")
                    mult_total += int(numbers[0]) * int(numbers[1])

    return mult_total


def part_1(input) -> int:
    correct_multiplications = []
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    mult_total = 0
    for line in input:
        correct_multiplications = re.findall(pattern, line)
        for m in correct_multiplications:
            mult_total += int(m[0]) * int(m[1])
    return mult_total

with open(os.path.join("inputs", "day3_input.txt"), "r") as input:
    print(f"(part 1) multiplication total = {part_1(input)}")
    print(f"(part 2) multiplication total = {part_2(input)}")

