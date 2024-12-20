class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        return sum([1 for index in range(len(arr))  if sum(arr[:index+1]) == index*(index+1)/2])
    

from inputs.variable_769 import *

sol = Solution()
print(sol.maxChunksToSorted(test2))     
