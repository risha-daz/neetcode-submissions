class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)

        for i in strs:
            s = [0 for _ in range(26)]
            for c in i:
                s[ord(c)-97]+=1
            mem[tuple(s)].append(i)
        return list(mem.values())