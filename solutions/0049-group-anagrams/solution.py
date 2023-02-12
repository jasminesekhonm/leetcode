class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramDict = defaultdict(list)
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString in anagramDict:
                anagramDict[sortedString].append(string)
            else:
                anagramDict[sortedString] = [string]
        
        return anagramDict.values()
