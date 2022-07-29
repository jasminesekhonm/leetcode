class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        len_prefix = min([len(string) for string in strs])
        
        result = 0
        
        for i in range(len_prefix):
            if len(set([ord(string[i]) for string in strs])) != 1:
                break 
            result += 1
            
        return strs[0][:result]
                
                
            
        
