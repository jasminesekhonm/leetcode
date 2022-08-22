class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNum = float('inf')
        secondNum = float('inf')
        for n in nums:
            if n <= firstNum:
                firstNum = n 
            elif n <= secondNum:
                secondNum = n 
            else:
                return True
        return False
