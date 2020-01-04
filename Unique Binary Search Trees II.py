# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(start, end):
            if start == end:
                return [None]
            if start +1 == end:
                return [TreeNode(start)]
            res = []
            for i in range(start, end):
                for ll in helper(start, i):
                    for rr in helper(i+1, end):
                        node = TreeNode(i)
                        node.left = ll
                        node.right = rr
                        res.append(node)
            return res
        if n == 0: return []
        return helper(1, n+1)