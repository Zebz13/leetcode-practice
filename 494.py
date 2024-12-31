class Solution:
    def recursive_value_calculator(self,nums,target,index,curr_sum,total_success,memo,total_sum):
        if index == len(nums):
            if curr_sum == target: 
                # print(memo)
                return 1
            else: 
                return 0
        else:
            if(memo[index][total_sum+curr_sum]!=float('-inf')):
                return memo[index][total_sum+curr_sum]
            add = self.recursive_value_calculator(nums,target,index+1,curr_sum+nums[index],total_success,memo,total_sum)
            sub = self.recursive_value_calculator(nums,target,index+1,curr_sum-nums[index],total_success,memo,total_sum)
            print(index,curr_sum,add,sub)
            memo[index][total_sum+curr_sum] = add + sub
            return memo[index][total_sum+curr_sum]
        
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo_table = [[float('-inf')] * (2*sum(nums)+1)  for _ in range(len(nums)) ]
        # print(memo_table)
        total_success = [0]
        return self.recursive_value_calculator(nums,target,0,0,total_success,memo_table,sum(nums))
         
    
from inputs.variable_494 import *

sol = Solution()
print(sol.findTargetSumWays(*test1)) 