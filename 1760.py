class Solution:
    def isDivisble(self,threshold,limitOperations,nums):
        operations = 0
        for num in nums:
            operations+= (num//threshold) + (num%threshold>0) - 1
            if(operations>limitOperations):
                return False
        return True


    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        right_pointer = max(nums)
        left_pointer = 1 #should be smallest positive number
        while left_pointer<=right_pointer:
            middle = (right_pointer+left_pointer)//2
            if(self.isDivisble(middle,maxOperations,nums)):
                right_pointer = middle-1
            else:
                left_pointer = middle+1
        return left_pointer


from inputs.variable_1760 import *

sol = Solution()
print(sol.minimumSize(*test1))