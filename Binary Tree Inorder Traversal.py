# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# In-order: Left->Current->Right
# Pre-order: Current->Left->Right
# Post-order: Left->Right->Current


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def DFS(result:List[int], root:TreeNode):
            if root is not None:
                DFS(result,root.left)
                result.append(root.val)
                DFS(result,root.right)
            else:
                return
        DFS(result, root)
        return result