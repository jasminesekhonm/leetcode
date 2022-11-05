class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        counter = 1
        tmp = a 
        while len(a) < len(b):
            a = a + tmp 
            counter += 1
        if b in a:
            return counter
        if b in a + tmp:
            return counter + 1 
        return -1
