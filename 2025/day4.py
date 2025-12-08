import sys
PAPER = '@'

maze = [line.strip() for line in sys.stdin.readlines()]

def neighbor_num(maze, r, c):
    # return the number of neighbors that are '@', 8-directionally
    num = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if i == r and j == c:
                continue
            if i >= 0 and i < len(maze) and j >= 0 and j < len(maze[0]):
                if maze[i][j] == PAPER:
                    num += 1
    return num

# count the number of '@' in the maze
num = 0
for r in range(len(maze)):
    for c in range(len(maze[0])):
        if maze[r][c] == PAPER and neighbor_num(maze, r, c) < 4:
            num += 1
print('part 1:', num)

remove_count = 0
removed = True
while removed:
    # simulate removing paper
    removed = False
    new_maze = []
    for r in range(len(maze)):
        new_row = []
        for c in range(len(maze[0])):
            if maze[r][c] == PAPER and neighbor_num(maze, r, c) < 4:
                remove_count += 1
                removed = True
            if maze[r][c] == PAPER and neighbor_num(maze, r, c) >= 4:
                new_row.append(PAPER)
            else:
                new_row.append('.')
        new_maze.append(new_row)
    print('new_maze', new_maze)
    print('remove_count', remove_count)
    maze = new_maze
print('part 2:', remove_count)