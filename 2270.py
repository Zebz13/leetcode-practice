from functools import lru_cache
class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        @lru_cache()
        def solve():
            valid_couhnt = 0
            nonlocal left_sum, right_sum
            for index in range(0,len(nums)-1):
                left_sum+=nums[index]
                right_sum-=nums[index]
                if left_sum>=right_sum:
                    valid_couhnt+=1
            return valid_couhnt
        return solve()
    
from inputs.variable_2270 import *

sol = Solution()
print(sol.waysToSplitArray(test2))