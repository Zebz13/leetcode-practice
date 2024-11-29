class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        result = [0] * n
        temp = code + code + code
        for index,c in enumerate(code):
            if(k>0):
                result[index] = sum(temp[index+1+n: n+k+index+1])
            if(k<0):
                result[index] = sum(temp[n+k+index:n+index])
            if(k==0):
                result[index] = 0
        return result
sol = Solution()
print(sol.decrypt([2,4,9,3],-2))