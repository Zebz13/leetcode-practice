class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        max_len = 0
        left = 0
        for right in range(len(nums)):
            while(nums[right]-nums[left]>2*k):
                left+=1
            max_len = max(max_len,right-left+1)
        return max_len
    
from inputs.variable_2779 import *

sol = Solution()
print(sol.maximumBeauty(*test3))