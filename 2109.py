class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        empty_str = ""
        temp = 0
        for i in spaces:
            empty_str+=s[temp:i]
            empty_str+=' '
            temp = i
        empty_str+=s[temp:]
        return empty_str
            
from inputs.variable_2109 import *

sol = Solution()
print(sol.addSpaces(*test1))