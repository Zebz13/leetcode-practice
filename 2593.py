import heapq
class Solution:
    def findScore(self, nums: list[int]) -> int:
        result = 0
        marked = [0] * len(nums)
        temp_nums = []
        for index,val in enumerate(nums):
            heapq.heappush(temp_nums,(val,index)) #sorted by val, tie break using index
        while(temp_nums):
            curr_val, curr_index = heapq.heappop(temp_nums)
            if(not marked[curr_index]):
                result+= curr_val
                marked[curr_index] = True
                if(0<=curr_index-1<len(nums)):
                    marked[curr_index-1] = True
                if(0<=curr_index+1<len(nums)):
                    marked[curr_index+1] = True
        return result


from inputs.variable_2593 import *

sol = Solution()
print(sol.findScore(test1))