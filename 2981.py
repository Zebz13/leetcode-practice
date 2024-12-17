class Solution:
    def maximumLength(self, s: str) -> int:
        frequency_counter = {}
        for i in range(len(s)):
            current_substring = []
            for j in range(i,len(s)):
                # print(current_substring,s[j])
                if(not current_substring or s[j] == current_substring[-1]):
                    current_substring.append(s[j])
                    str_list = "".join(current_substring)
                    if(str_list in frequency_counter):
                        frequency_counter[str_list] +=1
                    else:
                        frequency_counter[str_list] = 1
                else:
                    break
        # print(frequency_counter)
        max_len = -1
        for text_freq in frequency_counter:
            if(frequency_counter[text_freq]>=3):
                max_len = max(max_len,len(text_freq))
        return max_len
    
from inputs.variable_2981 import *

sol = Solution()
print(sol.maximumLength(test1))