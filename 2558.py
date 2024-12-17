import heapq, math
class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        temp_gift= []
        for i in gifts:
            heapq.heappush(temp_gift,-1*i)
        for i in range(k):
            curr_max_val = -1*heapq.heappop(temp_gift)
            # print(curr_max_val)
            adding_back = math.floor(math.sqrt(curr_max_val))
            heapq.heappush(temp_gift,-1*adding_back)
        return -1 * sum(temp_gift)
from inputs.variable_2558 import *

sol = Solution()
print(sol.pickGifts(*test1))
