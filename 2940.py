import heapq
class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        # 5 cases are present. 
        # 1. index_a>index_b and h_a>h_b-> index_a is the answer
        # 2. vice versa
        # 3. a and b are same points
        # 4. i_a>i_b and h_a<h_b
        # 5. i_a<i_b and h_a>h_b
        max_height_list = []
        index_of_queries = [[] for _ in heights]
        result = [-1 for _ in queries]
        for query_index,temp in enumerate(queries):
            index_a, index_b = temp
            if(index_a == index_b and heights[index_a] == heights[index_b]):
                result[query_index] = index_a
            elif(index_a>index_b and heights[index_a] > heights[index_b]):
                result[query_index] = index_a
            elif(index_a<index_b and heights[index_a] <heights[index_b]):
                result[query_index] = index_b
            else:
                index_of_queries[max(index_a,index_b)].append((max(heights[index_a],heights[index_b]),query_index))
        for index,height in enumerate(heights):
            while max_height_list and max_height_list[0][0]<height:
                _,ans_index = heapq.heappop(max_height_list)
                result[ans_index] = index
            for max_elem in index_of_queries[index]:
                heapq.heappush(max_height_list,max_elem)
        return result
    

from inputs.variable_2940 import *

sol = Solution()
print(sol.leftmostBuildingQueries(*test1)) 