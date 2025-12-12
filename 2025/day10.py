import sys

inputs = sys.stdin.readlines()

def convert_buttons_to_int(buttons):
    print('buttons', buttons)
    nums = buttons[1:-1].split(',')
#    print(nums)
    return sum([2**int(x) for x in nums if x])

def parse_input(input):
    # treat target as binary string and convert to int
    target = int(input.split(']')[0][1:][::-1].replace('.','0').replace('#','1'), 2)
    # treat numbers as an integer
    numbers = [convert_buttons_to_int(x) for x in input.split(']')[1].split('{')[0].strip().split(' ')]
    voltages = [int(x) for x in input.split('{')[1][:-2].split(',')]
    return target, numbers, voltages

def trace(target, pos, numbers, visited):
    min_steps = 99999
    for number in numbers[pos:]:
        if number in visited:
            continue
        visited.add(number)
        if target == number:
            #print('found', visited)
            min_steps = min(min_steps, len(visited))
            #print('min_steps', min_steps)
        steps = trace(target ^ number, pos+1, numbers, visited)
        min_steps = min(min_steps, steps)
        visited.remove(number)
    return min_steps

ans = 0
for input in inputs:
    target, numbers, voltages = parse_input(input)
    print(target, numbers, voltages)
    s = trace(target, 0, numbers, set())
    ans += s
print('part 1:', ans)