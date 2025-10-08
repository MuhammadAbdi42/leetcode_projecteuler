from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        distance = 1
        layer_nodes = [root]
        next_layer = []
        while layer_nodes != []:
            for node in layer_nodes:
                if node.left != None:
                    next_layer.append(node.left)
                if node.right != None:
                    next_layer.append(node.right)
            layer_nodes = next_layer
            next_layer = []
            if layer_nodes != []:
                distance += 1

        return distance
