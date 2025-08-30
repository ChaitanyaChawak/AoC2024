import sys
sys.setrecursionlimit(100000)


input = '/home/chai/Documents/AoC2024/puzzles/d06.txt'

with open(input, 'r') as file:
    input_lines = [line.strip() for line in file]

print(len(input_lines))
print(len(input_lines[0]))
visited = set()

def go_left(pos, grid, visited):
    y, x = pos
    visited.add(pos)
    #print(pos)
    try:
        next = grid[y][x-1]
        if next == '#': return go_up(pos, grid, visited)
        else:
            # print('left')
            return go_left((y, x-1), grid, visited)

    except:
    	print(next)
    	return visited

def go_down(pos, grid, visited):
    y, x = pos
    visited.add(pos)
    #print(pos)
    try:
        next = grid[y+1][x]
        if next == '#': return go_left(pos, grid, visited)
        else:
            # print('down')
            return go_down((y+1, x), grid, visited)

    except:
    	print(next)
    	return visited

def go_right(pos, grid, visited):
    y, x = pos
    visited.add(pos)
    #print(pos)
    try:
        next = grid[y][x+1]
        if next == '#': return go_down(pos, grid, visited)
        else:
            # print('right')
            return go_right((y, x+1), grid, visited)

    except:
    	print(next)
    	return visited

def go_up(pos, grid, visited):
    y, x = pos
    visited.add(pos)
    #print(pos)
    try:
        next = grid[y-1][x]
        if next == '#': return go_right(pos, grid, visited)
        else:
            # print('up')
            return go_up((y-1, x), grid, visited)

    except:
    	print(next)
    	return visited


for i in range(0, len(input_lines)):
    if '^' in input_lines[i]:
        go_up((i, input_lines[i].index('^')), input_lines, visited)
        

print(len(visited))

