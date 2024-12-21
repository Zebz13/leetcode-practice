from collections import defaultdict
class Solution:
    def recursive_tree_parser(self,curr_node,parent,adjDict,values,k,componentCount):
        sum_val = 0
        for adj_node in adjDict[curr_node]:
            if adj_node!=parent:
                sum_val+=self.recursive_tree_parser(adj_node,curr_node,adjDict,values,k,componentCount)
                sum_val = sum_val%k
        sum_val = sum_val+values[curr_node]
        sum_val = sum_val%k
        if(sum_val==0):
            componentCount[0]+=1
        return sum_val
        

    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        adj_dict = defaultdict(set)
        for start,end in edges:
            adj_dict[start].add(end)
            adj_dict[end].add(start)
        componentCount = [0]
        self.recursive_tree_parser(0,-1,adj_dict,values,k,componentCount)
        return componentCount[0]


from inputs.variable_2872 import *

sol = Solution()
print(sol.maxKDivisibleComponents(*test3))  