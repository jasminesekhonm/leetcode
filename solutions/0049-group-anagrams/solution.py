class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramDict = defaultdict(list)
        
        for string in strs:
            anagramDict[''.join(sorted(string))].append(string)
            
        return list(anagramDict.values())
        
            
        
