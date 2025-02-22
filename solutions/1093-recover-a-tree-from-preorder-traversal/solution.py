# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        index = 0 
        root = None 

        while index < len(traversal):
            depth = 0 
            while index < len(traversal) and traversal[index] == '-':
                depth += 1
                index += 1
            
            value = 0 
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1 
            
            node = TreeNode(value)
            if depth == 0:
                root = node 
            else:
                while len(stack) > depth:
                    stack.pop()

                if stack[-1][0].left == None:
                    stack[-1][0].left = node 

                else:
                    stack[-1][0].right = node 

            stack.append((node, depth))

        return root 
