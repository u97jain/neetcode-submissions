class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        for ch in s:
            sCount[ch] = 1 + sCount.get(ch, 0)
        
        tCount = {}
        for ch in t:
            tCount[ch] = 1 + tCount.get(ch, 0)
        
        return sCount == tCount