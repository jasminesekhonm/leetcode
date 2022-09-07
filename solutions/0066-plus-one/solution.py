class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        carry = 1
        i = len(digits) - 1
        while i >= 0 or carry:
            
            digit = 0
            
            if i >= 0: 
                digit = digits[i]
            
            sumVal = digit + carry
            if sumVal >= 10:
                currVal, carry = sumVal % 10, sumVal // 10
            else:
                currVal = sumVal
                carry = 0 
            res.append(currVal)
            i -= 1
        return res[::-1]
                
            
        
