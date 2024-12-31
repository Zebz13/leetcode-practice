# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
import heapq
class Solution:

    def find_swaps_required(self,level_values):
        print(level_values)
        swaps = 0
        target = sorted(level_values)

        # Map to track current positions of values
        pos = {val: idx for idx, val in enumerate(level_values)}

        # For each position, swap until correct value is placed
        for i in range(len(level_values)):
            if level_values[i] != target[i]:
                swaps += 1

                # Update position of swapped values
                cur_pos = pos[target[i]]
                pos[level_values[i]] = cur_pos
                level_values[cur_pos] = level_values[i]
        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        level_queue = [root]
        swaps_required = 0
        while(level_queue):
            level_size = len(level_queue)
            level_values = []
            for _ in range(level_size):
                node = level_queue.pop(0)
                level_values.append(node.val)
                print(node.val)
                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            swaps_required+=self.find_swaps_required(level_values)

        return swaps_required
    
from inputs.variable_2471 import *

sol = Solution()
print(sol.minimumOperations(TreeNode(test2))) 