class Solution:
    def minChanges(self, s: str) -> int:
        neighbor_xor = [int(s[i]) ^ int(s[i+1]) for i in range(0,len(s),2)]
        return sum(neighbor_xor)


a = input()

sol = Solution()
print(sol.minChanges(a))