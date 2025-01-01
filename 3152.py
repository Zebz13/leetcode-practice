class Solution:
    def binary_search(self,start,end,parity_breaks):
        left = 0
        right = len(parity_breaks)-1
        while(left<=right):
            middle = left+(right-left>>1)
            break_index = parity_breaks[middle]
            if(start>break_index):
                left = middle+1
            elif(end<break_index):
                right = middle-1
            else:
                return False
        return True


    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        res_arr = []
        parity_breaks = []
        for index in range(len(nums)-1):
            if(nums[index]%2==nums[index+1]%2):
                parity_breaks.append(index+1)
        for start,end in queries:
            res_arr.append(self.binary_search(start+1,end,parity_breaks))
        return res_arr

from inputs.variable_3152 import *

sol = Solution()
print(sol.isArraySpecial(*test2))