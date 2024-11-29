class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        result_set = []
        for i in range(n-k+1):
            flag = 0
            for j in range(1,k):
                if(i+j < n and nums[i+j-1]+1!=nums[i+j]):
                    flag = 1
            if(not flag):
                result_set.append(nums[i:i+k][k-1])
            else:
                result_set.append(-1)
        return result_set
sol =Solution()
print(sol.resultsArray([2,2,2,2],1))