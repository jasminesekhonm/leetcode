class Solution:
    def pivotInteger(self, n: int) -> int:
        p=n*(n+1)/2
        p=sqrt(p)
        if( p!=int(p) ):
            return -1
        return int(p)
