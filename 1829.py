class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        max_xor = 2**maximumBit - 1
        large_val = nums[0]
        output_list = [large_val ^ max_xor]
        for num in nums[1:]:
            large_val = large_val ^ num
            output_list.append(large_val ^ max_xor)
        return list(reversed(output_list))


sol = Solution()
print(sol.getMaximumXor([0,1,2,2,5,7],3))