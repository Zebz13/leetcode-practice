# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def find_largest_across_level(self,depth,node,output_list):
        if not node:
            return 0
        if depth==len(output_list):
            output_list.append(node.val)
        else:
            output_list[depth] = max(output_list[depth],node.val)
        
        self.find_largest_across_level(depth+1,node.left,output_list)
        self.find_largest_across_level(depth+1,node.right,output_list)


    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        print(root.__dict__)
        if(not root):
            return []
        else:
            layerwise_max=[]
            self.find_largest_across_level(0,root,layerwise_max)
        
        return layerwise_max

from inputs.variable_515 import *

sol = Solution()
print(sol.largestValues(TreeNode(test1))) 