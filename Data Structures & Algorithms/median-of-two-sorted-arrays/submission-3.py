class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 != 0:
            mid = len(nums)//2
            return float(nums[mid])
        mid = len(nums)//2
        return (nums[mid-1]+nums[mid])/2
