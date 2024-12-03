class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        count = 0
        for word in sentence.split(" "):
            count+=1
            if searchWord in word[0:len(searchWord)]:
                return count
        return -1
            
from inputs.variable_1455 import *

sol = Solution()
print(sol.isPrefixOfWord(*test4))