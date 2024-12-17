import heapq
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq_dict = {}
        for char in s:
            freq_dict[char] = freq_dict.get(char,0) + 1
        freq_list = [[-ord(s),freq,s] for s,freq in freq_dict.items()]
        heapq.heapify(freq_list)
        empty_list = []
        while(freq_list):
            str_value,str_count,str_char = heapq.heappop(freq_list)
            multiply_times = min(repeatLimit,str_count)
            empty_list.append(str_char*multiply_times)

            if(multiply_times<str_count and freq_list):
                snd_str_value,snd_str_count,snd_str_char = heapq.heappop(freq_list)
                empty_list.append(snd_str_char)
                snd_str_count-=1
                if(snd_str_count>0):
                    heapq.heappush(freq_list,[snd_str_value,snd_str_count,snd_str_char])
                heapq.heappush(freq_list,[str_value,str_count-multiply_times,str_char])
            # print(freq_list)
            # print(empty_list)
        return "".join(empty_list)
    

from inputs.variable_2182 import *

sol = Solution()
print(sol.repeatLimitedString(*test1))        