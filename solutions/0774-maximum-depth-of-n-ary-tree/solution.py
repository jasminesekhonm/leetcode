class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
            
        max_depth = 0
        
        def dfs(node, current_depth):
            nonlocal max_depth
            max_depth = max(max_depth, current_depth)
            
            if node.children:
                for child in node.children:
                    dfs(child, current_depth + 1)
        
        dfs(root, 1)  # Depth of a tree with just the root is 1
        return max_depth
