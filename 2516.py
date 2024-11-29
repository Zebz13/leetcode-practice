class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        sum_arr = [0,0,0] #a,b,c counts
        for char in s:
            sum_arr[ord(char)-ord('a')] +=1
        if(sum_arr[0]<k or sum_arr[1]<k or sum_arr[2]<k):
            return -1
        left = 0
        max_window = 0
        min_window = float('inf')
        inc_sum_arr = [0,0,0]
        for right in range(len(s)):
            inc_sum_arr[ord(s[right])-ord('a')] +=1
            while(sum_arr[0]-inc_sum_arr[0]<k or sum_arr[1]-inc_sum_arr[1]<k or sum_arr[2]-inc_sum_arr[2]<k):
                inc_sum_arr[ord(s[left])-ord('a')] -=1
                left+=1
            max_window = max(max_window,right-left+1)
        return len(s)-max_window
sol = Solution()
print(sol.takeCharacters("aabaaaacaabc",2))