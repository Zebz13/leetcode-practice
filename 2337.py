class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        # print(n)
        start_pointer = 0
        target_pointer = 0
        while(start_pointer<n or target_pointer<n):
            while(start_pointer<n and start[start_pointer]=='_'):
                start_pointer+=1
            
            while(target_pointer<n and target[target_pointer] == '_'):
                target_pointer+=1
            # print(start_pointer,target_pointer)
            if((start_pointer == n) or (target_pointer == n)):
                return start_pointer == target_pointer
            if(start[start_pointer]!=target[target_pointer] or
               (start[start_pointer] == 'L' and start_pointer<target_pointer)
               or (start[start_pointer] == 'R' and start_pointer>target_pointer)):
                return False
            start_pointer+=1
            target_pointer+=1
        return True


from inputs.variable_2337 import *

sol = Solution()
print(sol.canChange(*test4))