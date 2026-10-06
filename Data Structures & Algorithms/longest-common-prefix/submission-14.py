class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        if "" in set(strs):
            return ""
        
        last = sorted(strs)[len(strs) - 1]
        first = sorted(strs)[0]

        
        while i < len(first) and i < len(last) and first[i] == last[i]:
            res += first[i]
            i += 1
        return res