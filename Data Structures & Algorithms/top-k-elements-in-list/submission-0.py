class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            d[i] = d.get(i,0) + 1

        for c,n in d.items():
            freq[n].append(c)

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
