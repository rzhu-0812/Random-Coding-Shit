def check_directions(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)

    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]

    def check_direction(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    
    for x in range(rows):
        for y in range(cols):   
            if grid[x][y] == word[0]:
                for dx, dy in directions:
                    if check_direction(x, y, dx, dy):
                        count += 1
                        
    return count

def xmas_patterns(grid):
    rows, cols = len(grid), len(grid[0])

    def is_xmas(x, y):
        if (
            0 <= x - 1 < rows and 0 <= x + 1 < rows and
            0 <= y - 1 < cols and 0 <= y + 1 < cols
        ):
            top_left = grid[x - 1][y - 1]
            top_right = grid[x - 1][y + 1]
            center = grid[x][y]
            bottom_left = grid[x + 1][y - 1]
            bottom_right = grid[x + 1][y + 1]

            return (
                center == 'A' and 
                (((top_left == 'M' and top_right == 'M') and 
                 (bottom_left == 'S' and bottom_right == 'S')) or
                ((top_left == 'M' and top_right == 'S') and 
                 (bottom_left == 'M' and bottom_right == 'S')) or
                ((top_left == 'S' and top_right == 'S') and 
                 (bottom_left == 'M' and bottom_right == 'M')) or
                ((top_left == 'S' and top_right == 'M') and 
                 (bottom_left == 'S' and bottom_right == 'M')))
            )
        return False

    count = 0
    
    for x in range(rows):
        for y in range(cols):
            if is_xmas(x, y):
                count += 1

    return count


with open('input.txt', 'r') as i:
    lines = i.readlines()

char_lines = [list(line.strip()) for line in lines]
target = 'XMAS'

total_xmas = check_directions(char_lines, target)
total_xmas_patterns = xmas_patterns(char_lines)

print(total_xmas)
print(total_xmas_patterns)