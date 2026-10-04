class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in s:
            if i.isalnum():
                st+=i.lower()
        if len(st)<2:
            return True
        l = 0
        r = len(st)-1
        while r>l:
            if st[l] != st[r]:
                return False
            l+=1
            r-=1
        return True