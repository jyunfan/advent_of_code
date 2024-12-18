import heapq
from collections import defaultdict

maze = open('day16.input').read().strip().split('\n')

def show(maze):
    fid = open('day16.out','w')
    for row in maze:
        fid.write(''.join([str(x) for x in row]).replace('0',' ')+'\n')
    fid.close()

def newpos(pos, direction):
    r, c = pos
    match direction:
        case '<':
            return (r, c-1)
        case '>':
            return (r, c+1)
        case '^':
            return (r-1, c)
        case 'v':
            return (r+1, c)
        
def newdir_turnleft(d):
    return {'^': '<', '<': 'v', 'v': '>', '>': '^'}[d]

def newdir_turnright(d):
    return {'^': '>',
            '>': 'v',
            'v': '<',
            '<': '^'}[d]

def search(maze):
    R = len(maze)
    C = len(maze[0])
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S':
                pos = (0,r,c,'>')
            elif maze[r][c] == 'E':
                goal = (r, c)
    visited = set()
    q = [pos]
    while q:
        s, r, c, d = heapq.heappop(q)
        if (r, c, d) in visited:
            continue
        visited.add((r, c, d))
        #print(s, '(', r, c, ')', d)
        if (r, c) == goal:
            return s
        # forward
        nr, nc = newpos((r,c), d)
        if (nr, nc, d) in visited or maze[nr][nc] == '#':
            pass
        else:
            heapq.heappush(q, (s+1, nr, nc, d))
            #print('next:', s+1, nr, nc, d)

        # turn left
        nd = newdir_turnleft(d)
        if (r, c, nd) in visited:
            pass
        else:
            heapq.heappush(q, (s+1000, r, c, nd))
        
        
        # turn right
        nd = newdir_turnright(d)
        if (r, c, nd) in visited:
            pass
        else:
            heapq.heappush(q, (s+1000, r, c, nd))
        #break
        
def search2(maze):
    R = len(maze)
    C = len(maze[0])
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S':
                pos = (0,r,c,'>',r,c,'>')
            elif maze[r][c] == 'E':
                goal = (r, c)
    visited = set()
    future_visited = set()
    q = [pos]
    bestscore = {}
    prev = defaultdict(list)
    best = 1e+9
    current_score = None
    while q:
        s, r, c, d, pr, pc, pd = heapq.heappop(q)
        
        if s > best:
            break
        
        # I had a bug here
        #if r == 59 and c == 139:
        #    print(s, r, c, d)
        
        if (r,c,d) in bestscore:
            if s < bestscore[(r,c,d)]:
                bestscore[(r,c,d)] = s
                prev[(r,c,d)] = [(pr, pc, pd)]
            elif s == bestscore[(r,c,d)]:
                prev[(r,c,d)].append((pr, pc, pd))
        else:
            bestscore[(r,c,d)] = s
            prev[(r, c, d)] = [(pr, pc, pd)]
            
        if (r, c, d) in visited:
            continue
            
        visited.add((r, c, d))

        #print(s, '(', r, c, ')', d)
        if (r, c) == goal:
            best = min(best, s)
            continue
            
        # forward
        nr, nc = newpos((r,c), d)
            
        if maze[nr][nc] == '#':
            pass
        elif (nr, nc, d) in visited:
            pass
        else:
            heapq.heappush(q, (s+1, nr, nc, d, r, c, d))

        # turn left
        nd = newdir_turnleft(d)
            
        if (r, c, nd) in visited:
            pass
        else:
            heapq.heappush(q, (s+1000, r, c, nd, r, c, d))
        
        
        # turn right
        nd = newdir_turnright(d)
            
        if (r, c, nd) in visited:
            pass
        else:
            heapq.heappush(q, (s+1000, r, c, nd, r, c, d))


    
    s = [[0]*C for r in range(R)]
    q = []

    for d in '<^>v':
        p = (goal[0], goal[1], d)
        if p in bestscore and bestscore[p] == best:
            q.append(p)
    visited = set()
    tiles = set()
    while q:
        (r, c, d) = q.pop()
        if (r, c, d) in visited:
            continue
        #print(r,c)

        visited.add((r, c, d))
        tiles.add((r, c))
        s[r][c] += 1
            
        
        if (r, c, d) not in prev:
            continue
        for p in prev[(r,c,d)]:
            q.append(p)
    
#    for tile
    show(s)
    counter = 0
    for r in range(R):
        for c in range(C):
            if s[r][c]!=0:
                counter += 1
    return counter
    
print('part1', search(maze))
print('part2', search2(maze))

