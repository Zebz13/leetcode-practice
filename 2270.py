from functools import lru_cache
class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        left_prefix = [0]*len(nums)
        right_prefix = [0]*len(nums)
        sum1 = 0
        sum2 = 0
        for index in range(len(nums)):
            sum1+=nums[index]
            sum2+=nums[len(nums)-1-index]
            left_prefix[index] = sum1
            right_prefix[len(nums)-1-index] = sum2
        
        @lru_cache()
        def solve():
            valid_couhnt = 0
            for index in range(1,len(nums)):
                if(left_prefix[index-1]>=right_prefix[index]):
                    valid_couhnt+=1

            return valid_couhnt
        return solve()
    
from inputs.variable_2270 import *

sol = Solution()
print(sol.waysToSplitArray(test2))