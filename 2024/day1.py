import numpy as np
input_text=open('day1.input').read().strip()
inputs = [x.split() for x in input_text.split('\n')]
inputs = [(int(a), int(b)) for a,b in inputs]
A = np.array(inputs)
X = A[0:,0]
Y = A[0:,1]
X.sort()
Y.sort()
print('part_1', np.sum(np.abs(X-Y)))

from collections import Counter
rmap = Counter(Y)
print('part_2', np.sum([x * rmap.get(x, 0) for x in X]))
