class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l=0
        r=len(heights)-1
        while(l<r):
            res = (min(heights[l],heights[r]))*(r-l)
            if heights[l]<heights[r]:
                l+=1
            elif heights[r]<heights[l]:
                r-=1
            elif heights[l]==heights[r]:
                l+=1
            area = max(area,res)
        return area