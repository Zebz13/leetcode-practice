class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1]+[0]*high #[1,0,0,0,0,0]
        for length in range(1,high+1):
            if(length >= zero):
                dp[length] += dp[length-zero]
            if(length >= one):
                dp[length] += dp[length-one]
            dp[length] %= 10**9 + 7
        # print(dp)
        return sum(dp[low:high+1])

from inputs.variable_2466 import *
sol = Solution()
print(sol.countGoodStrings(*test1))
