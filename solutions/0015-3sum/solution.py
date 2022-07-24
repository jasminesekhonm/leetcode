class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2]
        # 0     1   2   3  4  5
        # [-4, 0, ]
        # at i = 0, nums[i] = -4 --> remaining_sum = 4 -->
        # -1 + 5, 0 + 4, 1 + 3, 2 + 2 
        
        if len(nums) < 3:
            return []
        
        
        
        def twoSum(nums, target):
            i = 0 
            j = len(nums) - 1
            outputs = []
            while i < j:
                if nums[i] + nums[j] == target:
                    outputs.append([nums[i], nums[j]])
                    i = i + 1
                elif nums[i] + nums[j] > target:
                    j = j - 1
                elif nums[i] + nums[j] < target:
                    i = i + 1
                
            return outputs
                
        
        i = 0
        outputs = []
        while i < len(nums) - 2 and nums[i] <= 0:
            remaining_ = twoSum(nums[i + 1:], -nums[i]) 
            if remaining_:
                for duplet in remaining_:
                    triplet = [nums[i]] + duplet
                    if not triplet in outputs:
                        outputs.append(triplet)
            i += 1
        return outputs
        
        
        
    
    
            
        
