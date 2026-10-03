class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ## for a given substring, find the most frequent character
        ## if freq[char] < len(substring)-k then update substring 

        def find_most_common(freq):
            max_freq = 0 
            for i in range(26):
                max_freq = max(max_freq, freq[i])
            return max_freq 

        n = len(s)

        freq = [0] * 26 

        max_len = max_freq = 0 
        i, j = 0, 0 

        while j < n:
            char = s[j]

            freq[ord(char) - ord('A')] += 1
            max_freq = find_most_common(freq)
            
            while (j - i + 1) - max_freq > k:
                freq[ord(s[i]) - ord('A')] -= 1
                i += 1 
                max_freq = find_most_common(freq)
            
            max_len = max(max_len, j - i + 1)
            j += 1 

        return max_len 

        
        

        
