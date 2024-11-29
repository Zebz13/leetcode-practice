from collections import deque
class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # row, col and length
        possible_moves = deque([(0, 0, 0)] if grid[0][0] == 0 else [(0, 0, 1)])
        visited = [[float('inf')] * cols for _ in range(rows)]
        # print(visited)
        single_cell_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while possible_moves:
            # print(possible_moves)
            row, col, movement_cost = possible_moves.popleft()
            if row == rows - 1 and col == cols - 1:
                return movement_cost
            for row_move, col_move in single_cell_moves:
                temp_row = row + row_move
                temp_col = col + col_move
                # print(temp_row, temp_col)
                # print(visited)
                if 0 <= temp_row < rows and 0 <= temp_col < cols and visited[temp_row][temp_col] == float('inf'):
                    if grid[temp_row][temp_col] == 1:
                        visited[temp_row][temp_col] = movement_cost+1
                        possible_moves.append((temp_row, temp_col, movement_cost + 1))
                    else:
                        visited[temp_row][temp_col] = movement_cost
                        possible_moves.appendleft((temp_row, temp_col, movement_cost))
        return visited[rows-1][cols-1]


from inputs.variable_2290 import *
sol = Solution()
print(sol.minimumObstacles(a))
