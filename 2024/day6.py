import numpy as np
import functools
data=open('day6.input').read().strip().split('\n')
maze = [list(row) for row in data]

## part 1
R = len(maze)
C = len(maze[0])

# Find the initial position of the guard
for r in range(R):
    for c in range(C):
        if maze[r][c] == '^':
            guard_init = (r,c,'^')

def outside(r, c):
    return r < 0 or r >= R or c < 0 or c >= C

# next face direction
nextf = {'^':'>', '>':'v', 'v':'<', '<':'^'}

# Find next position
def next_pos(guard, maze):
    r, c, f = guard
    match f:
        case '^':
            r -= 1
        case '>':
            c += 1
        case 'v':
            r += 1
        case '<':
            c -= 1
    if outside(r, c):
        return (r, c, f)
    if maze[r][c] == '#':
        f = nextf[f]
        r, c = guard[0], guard[1] # go back because of the obstacle
    return (r, c, f)

guard = guard_init
guard_stats = []  # record states
while True:
    guard_stats.append((guard[0], guard[1]))
    guard = next_pos(guard, maze)

    if outside(guard[0], guard[1]):
        break

# find all path (excluding face direction)
guard_path = set(map(lambda x: (x[0], x[1]), guard_stats))
print('part_1', len(guard_path))

## part 2
loop_count = 0
for r in range(R):
    for c in range(C):
        if maze[r][c] in ('^', '#'):
            continue
        
        # only need to place obstacle on the path that guard will go through
        if (r, c) not in guard_path:
            continue
            
        guard = guard_init
        backup = maze[r][c]
        maze[r][c] = '#'

        visited = set()  # Store all stats
        while True:
            visited.add(guard)
            guard = next_pos(guard, maze)

            if outside(guard[0], guard[1]):
                break

            if guard in visited:
                loop_count += 1
                break
        maze[r][c] = backup
print('part_2', loop_count)
