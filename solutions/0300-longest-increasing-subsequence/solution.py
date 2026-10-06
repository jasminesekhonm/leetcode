class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        ## inserting in a sorted list 

        res = [nums[0]]

        for num in nums[1:]:
            if num > res[-1]:
                res.append(num)

            else:
                i = 0 
                while num > res[i]:
                    i += 1
                res[i] = num 
            
        return len(res)


        
