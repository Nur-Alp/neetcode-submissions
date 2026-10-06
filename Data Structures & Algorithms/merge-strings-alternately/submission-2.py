class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        n, m = len(word1), len(word2)
        minlen = min(n, m)
        for i in range(minlen):
            res += word1[i] + word2[i]
        
        if n > m:
            res += word1[minlen : n]
        elif n < m:
            res += word2[minlen : m]
        return res
            