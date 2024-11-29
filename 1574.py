class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        right_pointer = n - 1
        while right_pointer>0 and arr[right_pointer] >= arr[right_pointer - 1] :
            right_pointer -= 1
        result = right_pointer  # temp hold, edge case for 0 as well
        # print(result)
        left_pointer = 0
        while left_pointer < right_pointer:
            while(right_pointer<n and arr[left_pointer]>arr[right_pointer]):
                right_pointer+=1
            if(left_pointer>0 and arr[left_pointer]<arr[left_pointer-1]):
                break
            result = min(result,right_pointer-left_pointer-1)
            left_pointer+=1
            
        return result
sol = Solution()
print(sol.findLengthOfShortestSubarray([6,3,10,11,15,20,13,3,18,12]))
# [1,2,3,10,4,2,3,5]
# [5,4,3,2,1]