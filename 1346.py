class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        value_dict = {}
        for i in arr:
            value_dict[i] = value_dict.get(i,0) + 1
        for i in (value_dict.keys()):
            if(i!=0 and i*2 in value_dict):
                return True
            elif(i==0 and value_dict[0]>1):
                return True
        return False

        
from inputs.variable_1346 import *

sol = Solution()
print(sol.checkIfExist(test1))