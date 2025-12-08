import sys

inputs = sys.stdin.readline().split(',')

def find_number(start, end):
    if len(start) % 2 == 1:
        start = str(10 ** len(start))
#        print('new start', start)
    if (len(end) % 2 == 1):
        end = str('9' * (len(end)-1))
#        print('new end', end)

    print('fixed', start, end)
    if len(start) > len(end):
        return 0

    # adjust start
    LS = len(start) // 2
    if start[:LS] < start[LS:]:
        ns = int(start[:LS]) + 1
    else:
        ns = int(start[:LS])
    
    LE = len(end) // 2
    if end[:LE] > end[LE:]:
        ne = int(end[:LE]) - 1
    else:
        ne = int(end[:LE])

    print('adjusted', ns, ne)
    if ns > ne:
        return 0

    # sum from ns to ne
    return sum(map(lambda x: int(str(x)*2), range(ns, ne+1)))

ans = 0
for input in inputs:
    (start, end) = input.split('-')
    end = end.strip()
    c = find_number(start, end)
    print(start, end, c)
    print('--------------------------------')
    ans += c
print('part 1:', ans)