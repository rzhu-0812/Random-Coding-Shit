from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def parse_maze(maze):
    n = len(maze)
    grid = []
    start = None
    moves = {}
    
    for i in range(n):
        row = []
        for j in range(0, len(maze[i]), 3):
            cell = maze[i][j:j+3]
            if cell == 'BBB':
                start = (i, j // 3)
                row.append('.')
            elif cell == '###':
                row.append('#')
            elif cell == '...':
                row.append('.')
            else:
                row.append('.')
                moves[(i, j // 3)] = cell
        grid.append(row)
    
    return grid, start, moves

def is_winning_board(board):
    for row in board:
        if ''.join(row) in ['MOO', 'OOM']:
            return True
    for col in range(3):
        if ''.join(board[row][col] for row in range(3)) in ['MOO', 'OOM']:
            return True
    if ''.join(board[i][i] for i in range(3)) in ['MOO', 'OOM']:
        return True
    if ''.join(board[i][2-i] for i in range(3)) in ['MOO', 'OOM']:
        return True
    return False

def bfs(grid, start, moves):
    n = len(grid)
    visited = set()
    queue = deque([(start[0], start[1], [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])])
    winning_boards = set()
    
    while queue:
        x, y, board = queue.popleft()
        
        state = (x, y, tuple(tuple(row) for row in board))
        if state in visited:
            continue
        visited.add(state)
        
        if is_winning_board(board):
            winning_boards.add(tuple(tuple(row) for row in board))
            continue
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '#':
                new_board = [row[:] for row in board]

                if (nx, ny) in moves:
                    move = moves[(nx, ny)]
                    char, i, j = move[0], int(move[1]) - 1, int(move[2]) - 1
                    if new_board[i][j] == '.':
                        new_board[i][j] = char

                queue.append((nx, ny, new_board))
    
    return winning_boards

if __name__ == "__main__":
    n = int(input())
    maze = [input() for _ in range(n)]
    
    grid, start, moves = parse_maze(maze)
    
    winning_boards = bfs(grid, start, moves)

    print(len(winning_boards))
    