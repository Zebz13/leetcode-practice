from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        cumulativeSum = 0
        left = 0
        temp_arr = defaultdict(int)
        n = len(nums)
        for right in range(n):
            cumulativeSum += nums[right]
            temp_arr[nums[right]] += 1
            if (
                right - left + 1 > k
            ):  # +1 used as we're using right and left for fetching values. and it starts from 0
                cumulativeSum -= nums[left]
                temp_arr[nums[left]] -= 1
                if temp_arr[nums[left]] == 0:
                    temp_arr.pop(nums[left])
                left += 1
            if right - left + 1 == k == len(temp_arr.keys()):
                result = max(result, cumulativeSum)
        return result


sol = Solution()
print(sol.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
