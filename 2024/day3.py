import numpy as np
input_text=open('day3.input').read().strip()
import re
input_text

def part1(input_text):
    s = 0
    # Use regular expression to find all mul(X,Y)
    for pair in re.findall(r"mul\([\d]{1,3},[\d]{1,3}\)", input_text):
        left, right = pair.split(",")
        left = int(left[4:])
        right = int(right[:-1])
        s += left * right
    return s

print('part_1', part1(input_text))

def part2(input_text):
    # Keep latest state
    enabled = True
    s = 0
    
    for instruction in re.findall("mul\([\d]{1,3},[\d]{1,3}\)|do\(\)|don't\(\)", input_text):
        if instruction.startswith("mul"):
            if enabled == False:
                continue
            left, right = instruction.split(",")
            left = int(left[4:])
            right = int(right[:-1])
            s += left * right
        elif instruction == 'do()':
            enabled = True
        else:
            enabled = False
        
    return s

print('part_2', part2(input_text))
