# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check(p, q):
            if not p and not q:
                return True
            elif (p and not q) or (q and not p):
                return False 
            elif (p.val != q.val):
                return False 

            return True 

        myq = deque() 
        visited = set()

        myq.append((p, q))

        while myq:
            curr_p, curr_q = myq.popleft()
            if not check(curr_p, curr_q):
                return False 
            if (curr_p and curr_q):
                myq.append((curr_p.left, curr_q.left))
                myq.append((curr_p.right, curr_q.right))

        return True 

        
        
