from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        freq_dict = defaultdict(list)

        for s in strs:
            freq = [0]*26
            for char in s:
                freq[ord(char)-ord('a')] += 1
            freq_dict[tuple(freq)].append(s)

        return list(freq_dict.values())
            

        

