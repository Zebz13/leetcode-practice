class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items = sorted(items)
        sorted_query = sorted([(price,index) for index,price in enumerate(queries)])
        output=[0] * len(queries)
        j=0
        max_beauty = 0
        for price,index in sorted_query:
            while j<len(items) and items[j][0] <= price:
                max_beauty = max(max_beauty,items[j][1])
                j+=1
            output[index] = max_beauty
        return output
sol = Solution()
print(sol.maximumBeauty([[1,1],[1000000000,1000000000],[2,2],[3,100000]],[1,2,3,1000000000]))