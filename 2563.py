class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        def bin_search(left_p,right_p,arr,limit):
            # print(left_p,right_p,arr)
            while(left_p<=right_p):
                middle_p = left_p + (right_p-left_p)//2
                if(arr[middle_p]>=limit):
                    right_p = middle_p - 1
                else:
                    left_p = middle_p + 1
            return right_p
        
        nums = sorted(nums)

        result = 0
        for i in range(len(nums)):
            lower_target = lower - nums[i]
            upper_target = upper - nums[i] 
            upper_numbers = bin_search(i+1,len(nums)-1,nums,upper_target+1)
            lower_numbers = bin_search(i+1,len(nums)-1,nums,lower_target)
            # print(upper_numbers,lower_numbers)
            result += upper_numbers - lower_numbers
        return result

sol = Solution()
print(sol.countFairPairs([7,5,6,9,4,2,10,3],10,13))