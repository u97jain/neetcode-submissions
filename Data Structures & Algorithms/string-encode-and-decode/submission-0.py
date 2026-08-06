class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for word in strs:
            encodedStr = encodedStr + str(len(word)) + '#' + word 
        return encodedStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            strLen = int(s[i:j])
            res.append(s[(j + 1) : (j + strLen + 1)])
            i = j + strLen + 1
        return res
        