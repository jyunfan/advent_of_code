from collections import Counter, defaultdict
stones = list(map(int, open('day11.smallinput').read().strip().split()))
print(stones)
def transform(S):
    ns = defaultdict(int)
    for s in S:
        count = S[s]
        ss = str(s)
        l = len(ss)//2
        if s == 0:
            ns[1] += count
        elif len(ss) % 2 == 0:
            #print(ss, l)
            ns[int(ss[:l])] += count
            ns[int(ss[l:])] += count
        else:
            ns[s * 2024] += count
    return ns

ps = Counter(stones)
for i in range(25):
    ps = transform(ps)
print('part_1', sum(ps.values()))

ps = Counter(stones)
for i in range(75):
    ps = transform(ps)
print('part_2', sum(ps.values()))
