from collections import defaultdict

input_text=open('day9.input').read().strip()

# part 1
c = 0
SPACE = -1
disk = []
for i in range(len(input_text)):
    if i % 2 == 1:
        disk.extend([SPACE] * int(input_text[i]))
    else:
        disk.extend([c] * int(input_text[i]))
        c += 1

n = len(disk)
left = 0
right = n - 1

while left < right:
    while disk[left] != SPACE:
        left += 1
    while disk[right] == SPACE:
        right -= 1
        
    # move disk[right] to disk[left]
    if left >= right:
        break
        
    disk[left] = disk[right]
    disk[right] = SPACE

result = disk
# check sum
s = 0
for i in range(len(result)):
    if result[i] != SPACE:
        s += i * int(result[i])

print('part1', s)

# part 2
# this time we use two lists
# space for number of blocks of the space(i)
# file for number of blocks of the file(i)
# note that len(file) == len(space)+1

space = []
file = []
for i in range(len(input_text)):
    if i % 2 == 1:
        space.append(int(input_text[i]))
    else:
        file.append(int(input_text[i]))

# defrag
nf = len(file)
# store the files moved to the space
file_in_space = defaultdict(list)
for i in range(nf-1, 0, -1):
    # move ID i to left most empty
    # search all space from left
    for k in range(i):
        if space[k] >= file[i]:
            #print('move file', i, 'to space', k)
            space[k] -= file[i]
            file_in_space[k].append([i, file[i]])
            file[i] = -file[i] # trick: mark that the file as empty
            break

# make result list
result = []
for i in range(nf):
    if file[i] > 0:
        # the file is not moved
        result.extend([i]*file[i])
    else:
        # the file is moved, fill SPACE (-1)
        result.extend([-1] * abs(file[i]))
        
    if i == nf-1:
        continue
    
    # add files which are moved to space
    for (file_id, num) in file_in_space[i]:
        result.extend([file_id]*num)
    result.extend([-1]*space[i])

# check sum
s = 0
for i in range(len(result)):
    if result[i] != SPACE:
        s += i * result[i]

print('part2', s)
