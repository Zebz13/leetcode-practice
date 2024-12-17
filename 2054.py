from heapq import *

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort(key = lambda x: x[0])
        endtime_heap = []
        max_temp_event_val = 0
        max_sequence_event_val = 0
        for event in events:
            while endtime_heap and endtime_heap[0][0]<event[0]:
                max_temp_event_val = max(max_temp_event_val,endtime_heap[0][1])
                heappop(endtime_heap)
            max_sequence_event_val = max(max_sequence_event_val,max_temp_event_val+event[2])
            heappush(endtime_heap,[event[1],event[2]])
        return max_sequence_event_val


from inputs.variable_2054 import *

sol = Solution()
print(sol.maxTwoEvents(test3))