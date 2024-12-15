import copy

maze = [list(row) for row in open('day15.input').read().strip().split('\n\n')[0].split('\n')]
inst = open('day15.input').read().strip().split('\n\n')[1].replace('\n','')

def show(maze):
    for row in maze:
        print(''.join(row))
        
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

def move(maze, robot, direction):
    R = len(maze)
    C = len(maze[0])
    (r, c) = newpos(robot, direction)
    
    if maze[r][c] == '#':
        return robot
    
    if maze[r][c] == '.':
        maze[r][c] = '@'
        maze[robot[0]][robot[1]] = '.'
        return (r, c)
    
    # run into box
    while maze[r][c] == 'O':
        r,c = newpos((r,c), direction)
        
    # hit wall, do nothing
    if maze[r][c] == '#':
        return robot
    
    # have space, move all boxes in front of the robot
    maze[r][c] = 'O'
    (r1, c1) = newpos(robot, direction)
    maze[r1][c1] = '@'
    maze[robot[0]][robot[1]] = '.'
    return (r1, c1)

def get_box_cod(maze):
    cod = 0
    R = len(maze)
    C = len(maze[0])
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'O':
                cod += r * 100 + c
    return cod

def expand(maze):
    M = []
    R = len(maze)
    C = len(maze[0])
    for r in range(R):
        row = []
        for c in range(C):
            s = maze[r][c]
            match s:
                case '#':
                    row.extend([s, s])
                case '.':
                    row.extend(['.', '.'])
                case 'O':
                    row.extend(['[', ']'])
                case '@':
                    row.extend(['@', '.'])
        M.append(row)
    return M


for r in range(len(maze)):
    for c in range(len(maze[0])):
        if maze[r][c] == '@':
            robot = (r, c)
            break

# Return all position of box
# special case: return [] if box hit wall
def travel_box(maze, init_pos, direction):
    # init pos
    # speical version DFS
    # [ -> ^, >
    # ] -> ^, <
    
    allpos = {}
    q = [init_pos]
    visited = set()
    hitwall = False
    while q:
        (r, c) = q.pop()
        if (r, c) in visited:
            continue
        #print((r,c))
        visited.add((r, c))
        
        s = maze[r][c]
        
        if s == '[':
            allpos[(r,c)] = s
            
            if direction == '^':
                # >
                if (r, c+1) not in visited:
                    q.append((r, c+1))
            
                # ^
                q.append((r-1, c))
            elif direction == 'v':
                # >
                if (r, c+1) not in visited:
                    q.append((r, c+1))
            
                # v
                q.append((r+1, c))
            elif direction == '<':
                q.append((r, c-1))
            elif direction == '>':
                q.append((r, c+1))
        elif s == ']':
            allpos[(r,c)] = s
            
            if direction == '^':
                # <
                if (r, c-1) not in visited:
                    q.append((r, c-1))

                # ^
                q.append((r-1, c))
            elif direction == 'v':
                # <
                if (r, c-1) not in visited:
                    q.append((r, c-1))

                # v
                q.append((r+1, c))
            elif direction == '<':
                q.append((r, c-1))
            elif direction == '>':
                q.append((r, c+1))
                
        elif s == '#':
            hitwall = True
        elif s == '.':
            pass
        else:
            error

    if hitwall:
        return {}
    else:
        return allpos

M = copy.deepcopy(maze)
for i in range(len(inst)):
    robot = move(M, robot, inst[i])
    #show(maze)

print('part1', get_box_cod(M))


maze2 = expand(maze)
for r in range(len(maze2)):
    for c in range(len(maze2[0])):
        if maze2[r][c] == '@':
            robot2 = (r, c)
            break
            
def get_box_cod2(M):
    cod = 0
    R = len(M)
    C = len(M[0])
    for r in range(R):
        for c in range(C):
            if M[r][c] == '[':
                cod += r * 100 + c
    return cod
                
M = copy.deepcopy(maze2)
pos = robot2
for i in range(len(inst)):
    #print(i, inst[i])
    (r, c) = newpos(pos, inst[i])
    
    if M[r][c] == '.':
        M[r][c] = '@'
        M[pos[0]][pos[1]] = '.'
        pos = (r, c)
        continue
    elif M[r][c] == '#':
        continue
    
    # run into box
    d = inst[i]
    boxes = travel_box(M, (r,c), d)

    if len(boxes) == 0:
        continue
    # clean
    for (r1,c1) in boxes:
        M[r1][c1] = '.'
    for (r1,c1) in boxes:
        s = boxes[(r1,c1)]
        if d == '^':
            M[r1-1][c1] = s
        elif d == 'v':
            M[r1+1][c1] = s
        elif d == '<':
            M[r1][c1-1] = s
        elif d == '>':
            M[r1][c1+1] = s
    M[pos[0]][pos[1]] = '.'
    M[r][c] = '@'
    pos = (r, c)

show(M)
print('part2', get_box_cod2(M))
