class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        s = set(nums)
        res = []
        for i in nums:
            length = 0
            while i-1 in s:
                length+=1
                i-=1
            res.append(length)

        return max(res)+1
    
                