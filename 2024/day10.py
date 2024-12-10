maze = open('day10.input').read().strip().split('\n')
def get_neighbor(r, c, R, C):
    ans = []
    if r > 0:
        ans.append((r-1, c))
    if r < R-1:
        ans.append((r+1, c))
    if c > 0:
        ans.append((r, c-1))
    if c < C-1:
        ans.append((r, c+1))
    return ans
    
R = len(maze)
C = len(maze[0])
starts = []
for r in range(R):
    for c in range(C):
        if maze[r][c] == '0':
            starts.append((r,c))


trails = 0
ratings = 0
for start in starts:
    visited = set([start])
    queue = [start]
    arrive = set()
    paths = []
    while queue:
        (r, c) = queue.pop()
        if maze[r][c] == '9':
            arrive.add((r,c))
            paths.append((r,c))
            
        for nei in get_neighbor(r,c, R, C):
            if int(maze[nei[0]][nei[1]]) == int(maze[r][c]) + 1 and not nei in visited:
                queue.append(nei)
    
    trails += len(arrive)
    ratings += len(paths)
    
    
print('part_1', trails)
print('part_2', ratings)
