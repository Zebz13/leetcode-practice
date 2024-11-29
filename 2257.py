class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        # m rows and n columns
        #address for grid_init will be (row,column)
        grid_init = [[0] * n for i in range(m)]
        
        for i,j in guards:
            grid_init[i][j]=1
        for i,j in walls:
            grid_init[i][j]=1
        direction_to_travel = [[0,1],[0,-1],[1,0],[-1,0]]
        for i,j in guards:
            for i_dir,j_dir in direction_to_travel:
                i_temp=i+i_dir
                j_temp=j+j_dir
                while(0<=i_temp<m and 0<=j_temp<n):
                    # print(i_temp,j_temp,grid_init[i_temp][j_temp])
                    if(grid_init[i_temp][j_temp]==1):
                        break
                    else:
                        grid_init[i_temp][j_temp]=2
                    # print(i_temp,j_temp,grid_init[i_temp][j_temp])
                    i_temp+=i_dir
                    j_temp+=j_dir
                    
        # print(grid_init)
        result = 0
        for i in range(m):
            for j in range(n):
                if(grid_init[i][j]==0):
                    result+=1
        return result
sol = Solution()
print(sol.countUnguarded(4,6,[[0,0],[1,1],[2,3]],[[0,1],[2,2],[1,4]]))