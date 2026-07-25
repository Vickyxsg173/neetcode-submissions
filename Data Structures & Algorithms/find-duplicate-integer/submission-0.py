class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for n in nums:
            d[n] = d.get(n,0)+1
        for k in d:
            if d[k]>1:
                return k