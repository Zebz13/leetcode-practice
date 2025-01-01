class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp_arr = [0] * (days[-1]+1)
        # print(len(dp_arr))
        arr_index = 0
        for day in range(1,days[-1]+1):
            if(day<days[arr_index]):
                dp_arr[day] = dp_arr[day-1]
            else:
                arr_index+=1
                dp_arr[day] = min(dp_arr[day-1]+costs[0],dp_arr[max(day-7,0)]+costs[1],dp_arr[max(day-30,0)]+costs[2])
        return dp_arr[-1]


from inputs.variable_983 import *

sol = Solution()
print(sol.mincostTickets(*test2)) 