class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        adjacent_list = [[i+1] for i in range (n-1)]
        output_list=[]
        for query in queries:
            adjacent_list[query[0]].append(query[1])
            init_list = [(0,0)] #start from 0 with traveled distance 0
            visited = set()
            visited.add(0)
            while init_list:
                current_loc,edges_traveled = init_list.pop(0)
                if(current_loc == n-1):
                    result= edges_traveled
                    break
                else:
                    for j in adjacent_list[current_loc]:
                        if(j not in visited):
                            init_list.append((j,edges_traveled+1))
                            visited.add(j)
            output_list.append(result)
        return output_list


sol = Solution()
print(sol.shortestDistanceAfterQueries(6,[[1,5],[2,4],[0,2],[0,4]]))