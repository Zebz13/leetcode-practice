class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        if(nums == sorted(nums)):
            return True
        else:
            sorted_region = []
            temp_list = []
            for count,num in enumerate(nums):
                curr_val = bin(num).count("1")
                if(not temp_list and not count):
                    temp_list.append(curr_val)
                if(not count):
                    prev_val = curr_val
                    temp_list.append(num)
                elif(count and (prev_val == curr_val)):
                    temp_list.append(num)
                elif(count and (prev_val != curr_val)):
                    sorted_region.append(temp_list)
                    prev_val=curr_val
                    temp_list=[curr_val,num]
                # print(prev_val,curr_val,count)
            sorted_region.append(temp_list)
            flag = True
            # print(sorted_region)
            for i in range(len(sorted_region)-1):
                # print(max(sorted_region[i]),min(sorted_region[i+1][1:]))
                if(max(sorted_region[i])>min(sorted_region[i+1][1:])):
                    return False
            return flag





nums = [8,4,2,5,15]
sol = Solution()
print(sol.canSortArray(nums))