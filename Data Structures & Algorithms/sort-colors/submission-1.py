class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(l,r):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp

        i,mid = 0,0
        j = len(nums)-1
        while mid<=j:
            if nums[mid] == 0:
                swap(i,mid)
                mid+=1
                i+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                swap(mid,j)
                j -=1
            
        