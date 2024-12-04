class Solution:
    def cyclic_converter(self,char):
        return chr(((ord(char) - ord('a') + 1) % 26)+ord('a'))
    
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str1_pointer = 0 
        str2_pointer = 0
        while(str1_pointer<len(str1) and str2_pointer<(len(str2))):
            if(str1[str1_pointer] == str2[str2_pointer] or self.cyclic_converter(str1[str1_pointer]) == str2[str2_pointer]):
                str1_pointer+=1
                str2_pointer+=1
            else:
                str1_pointer+=1
        return True if(str2_pointer== len(str2)) else False
    
from inputs.variable_2825 import *

sol = Solution()
print(sol.canMakeSubsequence(*test3))