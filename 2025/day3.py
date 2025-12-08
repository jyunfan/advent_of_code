
import sys
from itertools import accumulate, combinations

data = sys.stdin.readlines()
def solve(s, k, numbers):
    global cache
    if k == 0:
        return 0

    if s + k > len(numbers):
        return 0
    
    if (s, k) in cache:
        return cache[(s, k)]
    
    cache[(s, k)] = max(solve(s+1, k, numbers), solve(s+1, k-1, numbers) + numbers[s] * 10**(k-1))
    return cache[(s, k)]

ans = 0
for line in data:
    line = line.strip()
    numbers = list(map(int, line))
    combinations_of_2 = list(combinations(numbers, 2))
    maxv = 0
    for (a, b) in combinations_of_2:
        maxv = max(a*10+b, maxv)
    ans += maxv
print(ans)

ans_part2 = 0
for line in data:
    cache = {}
    numbers = list(map(int, line.strip()))
    print(numbers)
    solve(0, 12, numbers)
    print(cache[(0, 12)])
    ans_part2 += cache[(0, 12)]
print('part 2:', ans_part2)