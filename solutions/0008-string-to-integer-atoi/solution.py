class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        sign = 1
        index = 0
        intMax = 2**31 - 1
        intMin = 2**31
        while index < len(s) and s[index] == ' ':
            index += 1
        if index < len(s) and s[index] in '-+':
            sign = 1 if s[index] == '+' else -1 
            index += 1
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            num = num * 10 + digit
            index += 1
        
                
        num = sign * num
        if num > 2**31-1:
            return 2**31-1
        if num < -2**31:
            return -2**31
        return num
        
