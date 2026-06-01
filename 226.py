class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None

        # Recursive case
        tmp = root.right
        root.right = root.left
        root.left = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
