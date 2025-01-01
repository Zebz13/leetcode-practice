from collections import defaultdict
from functools import lru_cache 
class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        character_index_count = defaultdict(int)
        for word in words:
            for index, char in enumerate(word):
                character_index_count[(index, char)] = (
                    character_index_count.get((index, char), 0) + 1
                )
    
        lookup_table = [[-1] * len(target) for _ in range(len(words[0]))]
        @lru_cache()
        def dfs(target_index, word_index):
            if target_index == len(target):
                return 1
            if word_index == len(words[0]):
                return 0
            if lookup_table[word_index][target_index]!=-1:
                return lookup_table[word_index][target_index]
            # print(target_index)
            lookup_table[word_index][target_index] = dfs(target_index, word_index + 1)
            lookup_table[word_index][target_index] += character_index_count[
                (word_index, target[target_index])
            ] * dfs(target_index + 1, word_index + 1)
            return lookup_table[word_index][target_index] % (10**9 + 7)
        return dfs(0,0)


from inputs.variable_1639 import *

sol = Solution()
print(sol.numWays(*test3))
