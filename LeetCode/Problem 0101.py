from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        self.is_mirror = True
        self.check(root, root)

        return self.is_mirror

    def check(self, l: TreeNode, r: TreeNode):
        if l.val == r.val:
            if (l.left != None and r.right == None) or (l.left == None and r.right != None) or (l.right != None and r.left == None) or (l.right == None and r.left != None):
                self.is_mirror = False
                return
            else:
                if (l.left != None and r.right != None):
                    self.check(l.left, r.right)
                if (l.right != None and r.left != None):
                    self.check(l.right, r.left)
        else:
            self.is_mirror = False
            return
