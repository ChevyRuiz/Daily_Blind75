# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        inorderList = []
        self.inorderTraversal(root, inorderList)
        if len(inorderList) == 1:
            return ans

        for i in range(0, len(inorderList) - 1):
            if inorderList[i + 1] <= inorderList[i]:
                ans = False
                break
        return ans

    def inorderTraversal(self, root, list):
        if not root:
            return

        self.inorderTraversal(root.left, list)
        list.append(root.val)
        self.inorderTraversal(root.right, list)
