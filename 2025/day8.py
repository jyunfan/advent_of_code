import sys
import numpy as np
from collections import Counter
N = 10

inputs = sys.stdin.readlines()
inputs = [list(map(int, x.strip().split(','))) for x in inputs]
A = np.array(inputs)
L = len(inputs)
print('L', L)

D = np.zeros((L, L))
Q = []
for i in range(L):
    for j in range(L):
        D[i, j] = D[j, i] = np.linalg.norm(A[i] - A[j])
        if i < j:
            Q.append((D[i, j], (i, j)))
Q.sort()

S = {}
for i in range(L):
    S[i] = i

scount = 0
for i in range(N):
    (d, (i, j)) = Q[i]
    print(d, i, j, A[i], A[j])

    if S[i] == S[j]:
        print('already connected')
        continue
    scount += 1

    # connect i and j
    print('connect', i, j)
    k = min(S[i], S[j])
    s1 = S[i]
    s2 = S[j]
    for a in range(L):
        if S[a] in (s1, s2):
            S[a] = k

# find size of connected components
C = Counter(S.values())
print(C)
print(sorted(C.values())[-3:])
print('part 1', np.prod(sorted(C.values())[-3:]))

# part 2
pos = N
while scount < L - 1:
    (d, (i, j)) = Q[pos]
    pos += 1
    print(d, i, j, A[i], A[j])

    if S[i] == S[j]:
        print('already connected')
        continue
    scount += 1

    # connect i and j
    print('connect', i, j)
    print('scount', scount)
    k = min(S[i], S[j])
    s1 = S[i]
    s2 = S[j]
    for a in range(L):
        if S[a] in (s1, s2):
            S[a] = k
    
    last1 = i
    last2 = j

print(A[last1], A[last2])
print('part 2', A[last1][0] * A[last2][0])