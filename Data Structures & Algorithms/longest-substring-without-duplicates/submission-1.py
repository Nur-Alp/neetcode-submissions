class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        seen = set()
        while r < len(s) :
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                res = max(r - l, res)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
        return res

                    


            
        