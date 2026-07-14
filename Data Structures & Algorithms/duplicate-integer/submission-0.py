class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            s.add(i)
        if len(nums) == len(s):
            return False
        return True
        