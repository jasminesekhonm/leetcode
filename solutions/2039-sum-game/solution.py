class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum_left = sum_right = 0
        count_left = count_right = 0
        
        for i in range(half):
            if num[i] == '?':
                count_left += 1
            else:
                sum_left += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                count_right += 1
            else:
                sum_right += int(num[i])
                
        if (count_left + count_right) % 2 != 0:
            return True
            
        diff_sum = sum_left - sum_right
        diff_count = count_left - count_right
        
        return (diff_sum * 2 + diff_count * 9) != 0
