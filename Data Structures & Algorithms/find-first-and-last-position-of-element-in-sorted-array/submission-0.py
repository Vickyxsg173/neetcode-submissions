class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
    
            if nums[mid]==target:
                ans = mid
                break
        
            elif nums[mid]<target:
                l = mid+1
        
            elif nums[mid]>target:
                r=mid-1

        l=r=ans
        while l>=1:
            if nums[l-1]==nums[l]:
                 l-=1
            else:
                break
        
        while r<=len(nums)-2:
            if nums[r+1] == nums[r]:
                r+=1
            else:
                break
        if ans == -1:
            return[-1,-1]
        return [l,r]