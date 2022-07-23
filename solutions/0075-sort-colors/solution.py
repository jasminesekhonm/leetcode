class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [2, 0, 2, 1, 1, 0]
        # Edge Cases:
        # 1. duplicates 
        # 2. lengths 
        
        if len(arr) < 2:
            return arr 
        
        # [2,0,2,1,1,0]
        # 0, 1, 2 
        
        swap = True 
        while swap:
            swap = False
            for i in range(len(arr)-1):
                if arr[i] > arr[i + 1]:
                    arr[i + 1], arr[i] = arr[i], arr[i + 1]
                    swap = True 
                    break 
        
        
        
        
                        
                
            
            
