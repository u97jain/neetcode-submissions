class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [ [] for _ in range(len(nums) + 1)]
        
        freqCount = {}
        for n in nums:
            freqCount[n] = 1 + freqCount.get(n, 0)

        for key, val in freqCount.items():
            freq[val].append(key)
        
        for i in range(len(freq) - 1, -1, -1):
            for digit in freq[i]:
                res.append(digit)
                if len(res) == k:
                    return res

        return res










    