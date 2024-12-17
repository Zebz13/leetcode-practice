import heapq
class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        nums_index_heap = []
        for index,val in enumerate(nums):
            nums_index_heap.append([val,index])
        heapq.heapify(nums_index_heap)
        for _ in range(k):
            val,index = nums_index_heap[0]
            val = val*multiplier
            heapq.heapreplace(nums_index_heap,[val,index])
        nums = [0] * len(nums)
        for val,index in nums_index_heap:
            nums[index] = val
        return nums


from inputs.variable_3264 import *

sol = Solution()
print(sol.getFinalState(*test2))