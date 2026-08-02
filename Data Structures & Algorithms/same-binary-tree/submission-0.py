# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preOrder(root,res):
            if not root:
                res.append(None)
                return res
            res.append(root.val)
            preOrder(root.left,res)
            preOrder(root.right,res)

            return res

        x1 = preOrder(p,[])
        x2 = preOrder(q,[])
        return x1==x2