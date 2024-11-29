class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        large_bin = bin(max(candidates))[2:]
        starting_value = 0
        for i in range(len(large_bin)):
            count = 0
            for candidate in candidates:
                # if(i>=len(bin(candidate)[2:])):
                #     continue
                if(candidate & 1<<i):
                    count+=1
                    # print(candidate,bin(candidate)[2:],candidate & 1<<i,i,count)
            if(starting_value<count):
                starting_value = count
        return starting_value

sol = Solution()
print(sol.largestCombination([16,17,71,62,12,24,14]))