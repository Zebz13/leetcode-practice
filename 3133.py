# https://leetcode.com/problems/minimum-array-end/description/comments/2713918
#refer link for understanding merge
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n_bin = bin(n-1)[2:]
        x_bin = bin(x)[2:]
        val = len(n_bin) - x_bin.count('0')
        if(val > 0):
            x = '0'*val+x_bin
        else:
            x = x_bin
            n_bin = '0'*-val+n_bin
        
        counter = 0
        final_value = ''
        for bit in x:
            if(bit == '0'):
                final_value+=n_bin[counter]
                counter+=1
            else:
                final_value+=bit
        return(int(final_value,2))

sol = Solution()
print(sol.minEnd(1,4))