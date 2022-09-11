class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = str(num)
        if len(num) == 1:
            return True
        
        reversed1 = num[::-1].lstrip('0')
        reversed2 = reversed1[::-1].lstrip('0')
        return reversed2 == num
