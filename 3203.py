from collections import defaultdict
from math import ceil
from heapq import *
class Solution:

    def find_diameter(self,curr_node,parent_node,adj_list):
        max_diameter = 0
        max_child_paths = [0,0]

        for node in adj_list[curr_node]:
            if(node!=parent_node):
                neighbor_node_dia, neighbor_leaf_path =  self.find_diameter(node,curr_node,adj_list)
                max_diameter = max(max_diameter,neighbor_node_dia)
                heappush(max_child_paths,neighbor_leaf_path)
                heappop(max_child_paths)

        max_diameter = max(max_diameter,sum(max_child_paths))

        return [max_diameter,max(max_child_paths)+1]
    
    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        n = len(edges1)+1
        m = len(edges2) + 1

        def build_adj_graph(edges):
            adj = defaultdict(list)
            for n1,n2 in edges:
                adj[n1].append(n2)
                adj[n2].append(n1)
            return adj
        
        adj1 = build_adj_graph(edges1)
        adj2 = build_adj_graph(edges2)

        d1,_ = self.find_diameter(0,-1,adj1)
        d2,_ = self.find_diameter(0,-1,adj2)

        return max(d1,d2,ceil(d1/2)+ceil(d2/2)+1)

    

from inputs.variable_3203 import *

sol = Solution()
print(sol.minimumDiameterAfterMerge(*test1)) 