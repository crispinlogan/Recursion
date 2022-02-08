"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~1h29mins in
"""


# def insert_val_in_bst(root, val):
#     return




"""
Same as https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root, val):
        # easier to read and probably better option from video!
        if root is None:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

#         # my first attempt±
#         """get to bottom of tree of where we would insert the new node, and return the parent...then insert the new node"""
#         if root is None:
#             return TreeNode(val)

#         def helper(root, val, parent=None):
#             # base case
#             if root is None:
#                 return parent
#             # recursive case
#             if root.val > val:
#                 return helper(root.left, val, parent=root)
#             if root.val < val: # else # or just get rid of this line altogether and in-indent below line
#                 return helper(root.right, val, parent=root)

#         parent = helper(root, val)

#         if parent.val > val:
#             parent.left = TreeNode(val)
#         else: # if parent.val < val
#             parent.right = TreeNode(val)

#         return root