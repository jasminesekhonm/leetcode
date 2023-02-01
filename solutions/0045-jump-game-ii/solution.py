class Solution:
    def jump(self, nums: List[int]) -> int:
        
        q = deque()
        q.append((0, 0))

        visited = defaultdict(int)

        while q:
            currIdx, currJumps = q.popleft()
            if currIdx == len(nums) - 1:
                return currJumps 
            
            for newIdx in range(currIdx, min(currIdx + nums[currIdx] + 1, len(nums))):
                if newIdx not in visited or visited[newIdx] > currJumps + 1:
                    q.append((newIdx, currJumps + 1))
                    visited[newIdx] = currJumps + 1 
        
        return -1 

