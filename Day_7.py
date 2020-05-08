# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def level(root, ptr, lev):
    if root is None:
        return 0
    if root.val is ptr:
        return lev
    lvl = level(root.right, ptr, lev + 1)
    if lvl != 0:
        return lvl
    return level(root.left, ptr, lev + 1)
    
def sibling(root, a, b):
    if root is None:
        return False
    bb, rb, lb = False, False, False
    if (root.left is not None) and (root.right is not None):
        bb = ((root.left.val == a and root.right.val == b) or (root.left.val == b and root.right.val == a))
    if root.left is not None:
        lb = sibling(root.left, a, b)
    if root.right is not None:
        rb = sibling(root.right, a, b)
    return bb or lb or rb

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        return (level(root, x, 1) == level(root, y, 1)) and not sibling(root, x, y)
        
