class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        left = 0
        array_count = 0
        window = {}
        for right in range(len(nums)):
            window[nums[right]] = window.get(nums[right],0)+1
            while(abs(max(window) - min(window))>2):
                window[nums[left]] = window.get(nums[left],0) - 1
                if(window[nums[left]]<=0):
                    window.pop(nums[left])
                left+=1
            if(abs(nums[right] - nums[left])<=2):
                array_count+=right-left +1
            
        return array_count

from inputs.variable_2762 import *

sol = Solution()
print(sol.continuousSubarrays(test4))