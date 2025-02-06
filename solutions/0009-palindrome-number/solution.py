class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i = 0 
        j = len(x)-1
        
        while (i <= j and x[i] == x[j]):
            i += 1
            j -= 1
        
        return True if (i > j) else False

## Time Complexity: O(n)
## Space Complexity: O(1)

