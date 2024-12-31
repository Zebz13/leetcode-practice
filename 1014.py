class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_i,max_j,true_max_i = float('-inf'),float('-inf'),float('-inf')
        #optimize for j and take previous largest i
        for j in range(1,len(values)):
            i=j-1
            max_i = values[i]+i if values[i]+i > max_i else max_i
            if (max_i + values[j]-j) >max_j+true_max_i:
                max_j = values[j]-j 
                true_max_i = max_i
        return max_j+true_max_i
    
from inputs.variable_1014 import *

sol = Solution()
print(sol.maxScoreSightseeingPair(test4)) 