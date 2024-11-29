class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        in_degrees = [0] * n
        for edge in edges:
            in_degrees[edge[1]]+=1
        champ_count = 0
        champ = 0
        for count,in_degree in enumerate(in_degrees):
            if(in_degree==0):
                champ_count+=1
                champ=count
        return champ if champ_count==1 else -1

sol = Solution()
print(sol.findChampion(4,[[0,2],[1,3],[1,2],[1,0]]))
