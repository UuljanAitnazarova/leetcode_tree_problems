#700 leetcode problem


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursive approach
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            elif val > root.val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)
        return None 

#iterative approach
def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    current = root
    while current != None:
        if current.val == val:
            return current
        elif val > current.val:
            current = current.right
        else:
            current = current.left
    return None 