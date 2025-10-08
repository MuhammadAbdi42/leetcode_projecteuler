from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False

        self.is_same = True
        if p != None and q != None:
            self.check(p, q)

        return self.is_same

    def check(self, p: TreeNode, q: TreeNode):
        if p.val == q.val:
            if (p.right != None and q.right == None) or (p.right == None and q.right != None) or (p.left != None and q.left == None) or (p.left == None and q.left != None):
                self.is_same = False
                return

            if p.right != None and q.right != None:
                self.check(p.right, q.right)
            if p.left != None and q.left != None:
                self.check(p.left, q.left)
        else:
            self.is_same = False
            return
