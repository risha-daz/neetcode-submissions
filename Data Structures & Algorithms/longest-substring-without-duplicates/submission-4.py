class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        mem = {}
        res = 1
        left = 0
        mem[s[left]] = left
        for i in range(1,len(s)):
            if s[i] in mem:
                if mem[s[i]] >= left:
                    left = mem[s[i]]+1
                
            res = max(res, i - left + 1)
            mem[s[i]] = i
        return res