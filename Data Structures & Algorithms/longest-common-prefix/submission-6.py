class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        if "" in set(strs):
            return ""
        
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        return strs[0]