class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        # create window, but with bit counter, so that we can reverse OR operation
        window = [0] * 32
        window_left = 0
        or_value = 0
        min_len_sub_array=float('inf')
        for window_right,num in enumerate(nums):
            or_value |= num

            #window length
            for i in range(32):
                if(num & 1<<i):
                    window[i]+=1

            #perform catchup from left to right, once we get value 
            # - basic sliding window logic
            while(or_value>=k and window_left<=window_right):
                min_len_sub_array = min(min_len_sub_array,window_right-window_left+1) #0 based index. so len will be +1
                #remove left element-> basically remove bits count from window, for active bits of left value
                for i in range(32):
                    if(nums[window_left] & 1<<i):
                        window[i]-=1
                window_left+=1
                #recreating value after (removing left value above)
                or_value = 0
                for i in range(32):
                    if(window[i]):
                        or_value|= 1<<i 
        return min_len_sub_array if min_len_sub_array != float('inf') else -1

sol = Solution()
print(sol.minimumSubarrayLength([1,2],3))