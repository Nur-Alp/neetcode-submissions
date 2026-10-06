class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        minlen = min(len(word1), len(word2))
        for i in range(minlen):
            res += word1[i] + word2[i]
        
        if len(word1) > len(word2):
            res += word1[minlen : len(word1)]
        elif len(word1) < len(word2):
            res += word2[minlen : len(word2)]
        return res
            