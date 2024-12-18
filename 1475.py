class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        out_arr = []
        for i in range(len(prices)-1):
            discount = 0
            for j in range(i+1,len(prices)):
                if(prices[i]>=prices[j]):
                    discount = prices[j]
                    break
            out_arr.append(prices[i] - discount)
        out_arr.append(prices[-1])
        return out_arr
    

from inputs.variable_1475 import *

sol = Solution()
print(sol.finalPrices(test3))     