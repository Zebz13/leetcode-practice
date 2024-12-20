# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recursive_tree_parser(self, left, right, level):
        if(left == None):
            return 0
        if(right == None):
            return 0
        if(level % 2 != 0):
            temp_left = left.val
            left.val = right.val
            right.val = temp_left
        self.recursive_tree_parser(left.left,right.right,level+1)
        self.recursive_tree_parser(left.right,right.left,level+1)
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursive_tree_parser(root.left,root.right,-1)
        return root

        

from inputs.variable_2415 import *

sol = Solution()
print(sol.reverseOddLevels(TreeNode(test2)).__dict__)  