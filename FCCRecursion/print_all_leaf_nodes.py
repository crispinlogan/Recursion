"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~1h35mins in
"""


def print_all_leaf_nodes(node):
    """
    Traverse tree in whatever way you want, and when both .left and .right of
    the current node are None then print it
    """
    # base case
    if node is None: # in case a None is passed as the initial node
        return
    if node.left is None and node.right is None:
        print(node.val)
        return
    # recursive case
    print_all_leaf_nodes(node.left)
    print_all_leaf_nodes(node.right)




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

#         1
#      /    \
#    2       3
#   / \
# 4     5

print_all_leaf_nodes(root)