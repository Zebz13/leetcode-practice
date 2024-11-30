from collections import defaultdict
class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:  
        in_dict,out_dict = defaultdict(int),defaultdict(int)
        adjacent_list = defaultdict(list)
        for start,end in pairs:
            in_dict[end] += 1
            out_dict[start] += 1
            adjacent_list[start].append(end)
        start_node = -1
        for out in out_dict:
            if out_dict[out] == in_dict[out] + 1:
                start_node = out
                break
        

        if(start_node==-1):
            start_node = pairs[0][0]
        
        popping_list = [start_node]
        result = []
        while(popping_list):
            node = popping_list[-1]
            # print(node)
            if(adjacent_list[node]):
                popping_list.append(adjacent_list[node].pop(0))
            else:
                result.append(node)
                popping_list.pop()
        result.reverse()
        output_pair = [[result[i-1],result[i]] for i in range(1,len(result))]
        return output_pair


        
from inputs.variable_2097 import *

sol = Solution()
print(sol.validArrangement(test1))