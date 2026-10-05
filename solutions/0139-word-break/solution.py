class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        maxLen = max([len(w) for w in wordDict])
        n = len(s)
        wordSet = set(wordDict)
        dp = [True] + [False] * n
        for i in range(1, n+1):
            for j in range(max(0, i-maxLen), i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]

