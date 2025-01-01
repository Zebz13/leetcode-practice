class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        #3 SLIDING window approach
        #variables required - best sum for 3, current sum for 3, current index for all 3, return -> best index of all 3
        best_sum_one = sum(nums[:k])
        best_sum_two = best_sum_one + sum(nums[k:2*k])
        best_sum_three = best_sum_two + sum(nums[2*k:3*k])
        best_index_one = [0]
        best_index_two = [0,k]
        best_index_three = [0,k,2*k]

        index = 1
        while(3*k+index<=len(nums)):
            current_sum_one = sum(nums[index:k+index])
            if current_sum_one>best_sum_one:
                best_sum_one = current_sum_one
                best_index_one = [index]

            current_sum_two = best_sum_one + sum(nums[index+k:2*k+index])
            if current_sum_two>best_sum_two:
                best_sum_two = current_sum_two
                best_index_two = [best_index_one[0],k+index]
            current_sum_three = best_sum_two + sum(nums[2*k+index:3*k+index])
            if current_sum_three>best_sum_three:
                best_sum_three = current_sum_three
                best_index_three = [best_index_two[0],best_index_two[1],2*k+index]
            index+=1
        return best_index_three    

from inputs.variable_689 import *

sol = Solution()
print(sol.maxSumOfThreeSubarrays(*test1)) 