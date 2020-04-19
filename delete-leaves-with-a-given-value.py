# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        left = self.removeLeafNodes(root.left, target)
        right = self.removeLeafNodes(root.right, target)
        if left is None and right is None:
            if root.val == target:
                return None
            else:
                root.left, root.right = None, None
                return root
        else:
            root.left, root.right = left, right
            return root

if __name__ == '__main__':
    pass
