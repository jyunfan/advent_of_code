import sys

inputs = sys.stdin.readlines()
ranges = []

case = 1
ans = 0
for input in inputs:
    if case == 1:
        if input.strip() == '':
            case = 2
            continue
        (start, end) = input.split('-')
        ranges.append((int(start), int(end)))
    else:
        quest = int(input.strip())
        for (start, end) in ranges:
            if quest >= start and quest <= end:
                ans += 1
                break
print('part 1:', ans)

ans = 0
X = []
for (start, end) in ranges:
    X.append((start, '+'))
    X.append((end, '-'))
X.sort()

depth = 0
valid_count = 0
prev_k = 0
for (k, s) in X:
    if depth > 0:
        valid_count += k - prev_k
        print('valid += ', k, k - prev_k)
    else:
        # new section
        if s != '+':
            raise Exception('Invalid section')
        valid_count += 1
        print('valid += ', k, 1)
    if s == '+':
        depth += 1
    else:
        depth -= 1
    print(k, depth)
    print('--------------------------------')
    prev_k = k
print(X)
print('part 2:', valid_count)