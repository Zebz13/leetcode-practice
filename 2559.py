from functools import lru_cache

class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowel_list_sum = [0] * len(words)
        vowels = {"a","e","i","o","u"}
        prefix_sum = 0
        
        for index,word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum+=1
            vowel_list_sum[index] = prefix_sum
        
        @lru_cache()
        def prefix_sum():
            output = []
            for start,end in queries:
                output.append(vowel_list_sum[end] - (vowel_list_sum[start-1] if start else 0))
            return output
        return prefix_sum()
    

from inputs.variable_2559 import *

sol = Solution()
print(sol.vowelStrings(*test1))