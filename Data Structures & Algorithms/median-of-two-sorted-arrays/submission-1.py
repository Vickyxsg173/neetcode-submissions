class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        i = 0
        j = len(nums)-1
        if len(nums)%2 != 0:
            while i!=j:
                i+=1
                j-=1
            return float(nums[i])
        while i<j:
            i+=1
            j-=1
        return (nums[i]+nums[j])/2
