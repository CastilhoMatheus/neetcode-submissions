# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validateSubRoot(self, node1, node2):

        if node1 and not node2:
            return False
        
        elif node2 and not node1:
            return False
        
        elif not node1 and not node2:
            return True
        
        elif node1.val != node2.val:
            return False
        
        left, right = self.validateSubRoot(node1.left, node2.left), self.validateSubRoot(node1.right, node2.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        flag = False

        while q:
            node = q.popleft()

            if node.val == subRoot.val:
                flag = self.validateSubRoot(node, subRoot)
                if flag:
                    break
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)


        return flag