class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        negative_counter = 0
        cumulative_sum=0
        min_value = float('inf')
        for rows in matrix:
            for col in rows:
                cumulative_sum+=abs(col)
                min_value=min(abs(col),min_value)
                if(col<0):
                    negative_counter+=1
        print(cumulative_sum,negative_counter)
        if(negative_counter%2==0):
            return cumulative_sum
        else:
            return cumulative_sum-2*min_value #since we're adding, reduce that + reduce cause negative


sol = Solution()
print(sol.maxMatrixSum([[10000,10000,10000],[10000,10000,10000],[10000,10000,10000]]))