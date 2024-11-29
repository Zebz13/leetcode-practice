import heapq


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        # only case for -1
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1
        directions_to_move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        #heapq for ordering by 
        grid_cost = [(0, 0, 0)]
        visited = set((0, 0))
        while grid_cost:
            cost, row, col = heapq.heappop(grid_cost)
            if row == rows - 1 and col == cols - 1:
                return cost
            for row_move, col_move in directions_to_move:
                temp_row = row + row_move
                temp_col = col + col_move
                if (
                    0 <= temp_row < rows
                    and 0 <= temp_col < cols
                    and (temp_row, temp_col) not in visited
                ):
                    
                    if grid[temp_row][temp_col] <= cost + 1:
                        heapq.heappush(grid_cost,(cost + 1,temp_row, temp_col))
                    else:
                        # print(temp_row, temp_col,cost)
                        # print(grid_cost)
                        if (grid[temp_row][temp_col] - cost) % 2:
                            temp_cost =  grid[temp_row][temp_col] - cost
                        else:
                            temp_cost = grid[temp_row][temp_col] - cost + 1
                        # grid_cost.append((temp_row, temp_col, cost + temp_cost))
                        heapq.heappush(grid_cost,(cost + temp_cost,temp_row, temp_col))
                    visited.add((temp_row, temp_col))


from inputs.variable_2577 import *

sol = Solution()
print(sol.minimumTime(test1))
