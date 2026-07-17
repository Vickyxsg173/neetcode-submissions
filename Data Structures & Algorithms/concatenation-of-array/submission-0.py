class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x=len(nums)
        nums[x:] = nums
        return nums