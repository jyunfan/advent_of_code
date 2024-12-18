from collections import deque

blockers = open('day18.input').read().strip().split('\n')
N = 71

def make_maze(blockers, N, bn):
    maze = [['#'] + [' ']*N + ['#'] for r in range(N)]
    maze = [list(['#']*(N+2))] + maze + [list(['#']*(N+2))]

    for blocker in blockers[:bn]:
        x, y = blocker.split(',')
        x = int(x)
        y = int(y)
        maze[y+1][x+1] = '#'
    return maze


def show(maze):
    #fid = open('day16.out','w')
    for row in maze:
        print(''.join([str(x) for x in row]))
    #fid.close()
    
def nei(x, y):
    return [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]

def search(maze):
    R = len(maze)
    C = len(maze[0])
    visited = set()
    q = deque([(1,1,0)])
    #print(q)
    while q:
        x, y, step = q.popleft()
        #print(x,y,step)
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if x == N and y == N:
            break
        
        neis = nei(x, y)
        for (px, py) in neis:
            if (px, py) in visited or maze[py][px] == '#':
                continue
            q.append((px, py, step+1))
    #print("x,y,s", x, y, step)
    if x == N and y == N:
        return step
    else:
        return -1

print('part_1', search(make_maze(blockers, N, 1024)))

# Need about 6 seconds on my mac
for i in range(4000):
    maze = make_maze(blockers, N, i)
    if search(maze) == -1:
        break
print('part_2', blockers[i-1])
