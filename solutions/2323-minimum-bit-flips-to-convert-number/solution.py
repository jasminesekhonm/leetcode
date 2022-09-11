class Solution(object):
    def minBitFlips(self, start, goal):
        res = start ^ goal # finds the number of bits that are different
        cnt = 0
        while res:
            res &= res - 1 # number of 1s 
            cnt += 1
        return cnt
