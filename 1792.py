import heapq
class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        incremental_pct = []
        for pass_stud, total_stud in classes:
            pass_pct = pass_stud/total_stud
            inc_pct = pass_pct - (pass_stud+1)/(total_stud+1)
            heapq.heappush(incremental_pct,[inc_pct,pass_pct,pass_stud,total_stud])
        while(extraStudents>0):
            extraStudents-=1
            _,pass_pct,pass_stud,total_stud = incremental_pct[0]
            pass_stud+=1
            total_stud+=1
            pass_pct = pass_stud/total_stud
            inc_pct = pass_pct - (pass_stud+1)/(total_stud+1)
            heapq.heapreplace(incremental_pct,[inc_pct,pass_pct,pass_stud,total_stud])
            # print(incremental_pct)
        return sum([i[1] for i in incremental_pct])/len(incremental_pct)

from inputs.variable_1792 import *

sol = Solution()
print(sol.maxAverageRatio(*test2))