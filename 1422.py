class Solution:
    def maxScore(self, s: str) -> int:
        one_count = 0
        for i in s:
            if(i=='1'):
                one_count+=1
        max_score = 0
        score = 0
        for i in s[:-1]:
            if i == '0':
                score +=1
            else:
                one_count -=1
            max_score = max(max_score,score+one_count)
        return max_score

from inputs.variable_1422 import *

sol = Solution()
print(sol.maxScore(test1)) 