input = '/home/chai/Documents/AoC2024/puzzles/d04.txt'

with open(input, 'r') as file:
    input_lines = [line.strip() for line in file]

count = 0

#horizontals
for i in input_lines:
    count += i.count('XMAS')

    irev = i[::-1]
    count += irev.count('XMAS')

#verticals
def get_verticals(matrix):
    vertical = []
    height = len(matrix)
    for i in range(0, len(matrix[0])):
        j = 0
        vert = ''
        while j < height:
            vert += matrix[j][i]
            j += 1
        vertical.append(vert)
    return vertical

vert = get_verticals(input_lines)
for i in vert:
    count += i.count('XMAS')

    irev = i[::-1]
    count += irev.count('XMAS')


#diagonals
def get_diagonals(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # List to store all diagonals
    diagonals = []

    # Get main diagonals (top-left to bottom-right)
    for col in range(cols):
        diagonal = ''
        r, c = 0, col
        while r < rows and c < cols:
            diagonal += matrix[r][c]
            r += 1
            c += 1
        diagonals.append(diagonal)

    for row in range(1, rows):
        diagonal = ''
        r, c = row, 0
        while r < rows and c < cols:
            diagonal += matrix[r][c]
            r += 1
            c += 1
        diagonals.append(diagonal)

    # Get anti-diagonals (top-right to bottom-left)
    for col in range(cols):
        diagonal = ''
        r, c = 0, col
        while r < rows and c >= 0:
            diagonal += matrix[r][c]
            r += 1
            c -= 1
        diagonals.append(diagonal)

    for row in range(1, rows):
        diagonal = ''
        r, c = row, cols - 1
        while r < rows and c >= 0:
            diagonal += matrix[r][c]
            r += 1
            c -= 1
        diagonals.append(diagonal)
    
    return diagonals

diag = get_diagonals(input_lines)
for i in diag:
    count += i.count('XMAS')

    irev = i[::-1]
    count += irev.count('XMAS')

print(count)


#PART2

def x_mas(i, j, grid):
    diag1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
    diag2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]

    if (diag1 == 'MAS' or diag1[::-1] == 'MAS') and (diag2 == 'MAS' or diag2[::-1] == 'MAS'):
        return True
    else:
        return False

count2 = 0
for i in range(1, len(input_lines)-1):
    for j in range(1, len(input_lines[0])-1):
        if input_lines[i][j] == 'A' and x_mas(i,j, input_lines): count2 += 1

print(count2)


