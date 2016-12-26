# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def minRight(root):
            if root.left is None:
                return root.val
            return minRight(root.left)

        if root is None:
            return root
        if key == root.val and root.left is None and root.right is None:
            return None

        if key == root.val and root.left is None:
            return root.right

        if key == root.val and root.right is None:
            return root.left

        if key == root.val:
            root.val = minRight(root.right)
            root.right = self.deleteNode(root.right, root.val)
            return root

        if key>root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            root.left = self.deleteNode(root.left, key)
            return root
