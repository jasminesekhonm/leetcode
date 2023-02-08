class Solution:
    def rob(self, nums: List[int]) -> int:

        q = []

        maxSum = -float('inf')

        for i, num in enumerate(nums):
            q.append([num, i])

        visited = defaultdict(int) 

        while q:
            currNum, currIdx = q.pop()
            maxSum = max(maxSum, currNum)
            for i in range(currIdx+2, len(nums)):
                if i not in visited or visited[i] < (currNum + nums[i]):
                    q.append((currNum + nums[i], i))
                    visited[i] = currNum + nums[i]

        return maxSum 


        
