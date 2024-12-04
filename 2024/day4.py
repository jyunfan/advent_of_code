import numpy as np
input_text=open('day4.input').read().strip()

def is_xmas(text):
    return text == 'XMAS' or text == 'SAMX'

N = 4
def get_vertical(puzzle, r, c, R):
    return ''.join([puzzle[i][c] for i in range(r, min(r+N, R))])

def get_diag1(puzzle, r, c, R, C):
    text = []
    for i in range(N):
        if r+i < R and c+i < C:
            text.extend([puzzle[r+i][c+i]])
    return ''.join(text)

def get_diag2(puzzle, r, c, R, C):
    text = []
    for i in range(N):
        if r+i < R and c-i >= 0:
            text.extend([puzzle[r+i][c-i]])
    return ''.join(text)

def part1(input_text):
    puzzle = input_text.split('\n')
    R = len(puzzle)
    C = len(puzzle[0])
    counter = 0
    for r in range(R):
        for c in range(C):
            # horizontal
            word = puzzle[r][c:c+N]
            if is_xmas(word):
                counter += 1
            # vertical
            word = get_vertical(puzzle, r, c, R)
            if is_xmas(word):
                counter += 1
            # diag 1
            word = get_diag1(puzzle, r, c, R, C)
            if is_xmas(word):
                counter += 1
            word = get_diag2(puzzle, r, c, R, C)
            if is_xmas(word):
                counter += 1
    return counter

def match(board, r, c, pat):
    for i in range(3):
        for j in range(3):
            if pat[i][j] != '.' and pat[i][j] != board[r+i][c+j]:
                return False
    return True

def part2(input_text):
    board = input_text.split('\n')
    R = len(board)
    C = len(board[0])
    counter = 0
    M = 3
    for pat in [['M.S', '.A.', 'M.S'], ['M.M', '.A.', 'S.S'], ['S.S', '.A.', 'M.M'], ['S.M', '.A.', 'S.M']]:
        for r in range(R-M+1):
            for c in range(C-M+1):
                if match(board, r, c, pat):
                    counter += 1
    return counter

print('part_1', part1(input_text))
print('part_2', part2(input_text))


