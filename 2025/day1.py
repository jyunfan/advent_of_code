import sys
from itertools import accumulate

convert_to_int = lambda x: int(x.strip()[1:]) * -1 if x[0] == 'L' else int(x.strip()[1:])
data = list(map(convert_to_int, sys.stdin.readlines()))

# part 1
nums = list(accumulate(data, initial=50))
ans = list(map(lambda x: x % 100 == 00, nums)).count(True)

print(ans)

# part 2
c = 0
for i in range(1, len(nums)):
    a = nums[i-1]
    b = nums[i]
    l1 = a // 100
    l2 = b // 100

    if a >= b:
        if a % 100 == 0 and b % 100 != 0:
            c += abs(l1 - l2) - 1
        elif a % 100 != 0 and b % 100 == 0:
            c += abs(l1 - l2) + 1
        else:
            c += abs(l1 - l2)
    else:
        c += abs(l1 - l2)

print(c)