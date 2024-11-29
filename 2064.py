class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def canDistribute(k):
            stores_required = 0
            for quantity in quantities:
                stores_required += -(-quantity//k)
                # print(-(-quantity//k),quantity,k)
            # print(stores_required)
            return stores_required<=n

        right_p = max(quantities)
        left_p = 1 #min 1 item 
        result = 0
        while(left_p<=right_p):
            middle_p = left_p + (right_p - left_p) // 2
            if(canDistribute(middle_p)):
                right_p = middle_p - 1
                result = middle_p
            else:
                left_p = middle_p + 1
        return result

sol = Solution()
print(sol.minimizedMaximum(6,[11,6]))