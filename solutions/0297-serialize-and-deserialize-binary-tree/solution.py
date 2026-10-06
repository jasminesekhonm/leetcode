# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res, q = [], deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
            

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")

        if len(vals) == 0 or vals[0] == "null":
            return None 

        prev_node = root = TreeNode(val = int(vals[0]))

        i = 1
        
        q = deque([root])

        while q:
            curr = q.popleft()
            if vals[i] != "null":
                curr.left = TreeNode(int(vals[i]))
                q.append(curr.left)
            i += 1
            if i < len(vals) and vals[i] != "null":
                curr.right = TreeNode(int(vals[i]))
                q.append(curr.right)
            i += 1
        
        return root




                
                    





# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
