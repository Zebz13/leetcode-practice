class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        empty_list = set([i for i in range(1,n+1)])
        for ban in banned:
            empty_list.discard(ban)
        empty_list = list(empty_list)
        sum_var = sum(empty_list)
        while sum_var>maxSum:
            sum_var-=empty_list.pop()
        return len(empty_list)
    
from inputs.variable_2554 import *

sol = Solution()
print(sol.maxCount(*test1))