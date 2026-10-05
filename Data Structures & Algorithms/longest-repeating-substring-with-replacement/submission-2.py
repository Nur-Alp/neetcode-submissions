class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        seen = {}
        l, r = 0, 0
        for r, char in enumerate(s):
            seen[char] = 1 + seen.get(char, 0)
            while (r + 1 - l) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r + 1 - l)

        return res
