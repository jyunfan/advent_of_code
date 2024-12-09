import numpy as np
import functools
input_text=open('day5.input').read().strip()
rules, updates = input_text.split('\n\n')
rules = [[int(y) for y in x.split('|')] for x in rules.split('\n')]
updates = [[int(y) for y in x.split(',')] for x in updates.split('\n')]

# Get all pages
nums = set()
for rule in rules:
    nums.add(rule[0])
    nums.add(rule[1])

ruleset = set()
for rule in rules:
    ruleset.add((rule[0], rule[1]))

def cmp(a, b):
    if (a,b) in ruleset:
        return -1
    elif (b,a) in ruleset:
        return 0

# Sort pages by rules
sorted(nums, key=functools.cmp_to_key(cmp))

# part 1
ans = 0
K = len(rules)
for update in updates:
    n = len(update)
    fix = sorted(update, key=functools.cmp_to_key(cmp))
    # If the update is good (no need to fix)
    if fix == update:
        ans += update[n//2]
print('part1', ans)

# part 2
ans = 0
K = len(rules)
for update in updates:
    n = len(update)
    fix = sorted(update, key=functools.cmp_to_key(cmp))
    if fix != update:
        ans += fix[n//2]
print('part2', ans)
