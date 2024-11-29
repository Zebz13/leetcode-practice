from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        unique_xor = defaultdict(int)
        for row in matrix:
            if(row[0]):
                unique_xor[str(row)]+=1
            else:
                flipped_row = str([1 if i==0 else 0 for i in row])
                unique_xor[flipped_row]+=1
        return max(unique_xor.values())
sol = Solution()
print(sol.maxEqualRowsAfterFlips([[0,1],[1,1]]))