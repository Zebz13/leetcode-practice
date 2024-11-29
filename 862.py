import heapq


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        my_min_heap = []  # sum_value,index
        result = float("inf")
        continuous_sum = 0
        for index, num in enumerate(nums):
            continuous_sum += num
            if continuous_sum >= k:
                result = min(result, index + 1)
            while my_min_heap and continuous_sum - my_min_heap[0][0] >= k:
                result = min(result, index - heapq.heappop(my_min_heap)[1])
            heapq.heappush(my_min_heap, (continuous_sum, index))
        return result if result != float("inf") else -1


sol = Solution()
print(sol.shortestSubarray([2, -1, 2, 1], 3))
