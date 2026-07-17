class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                height = min(heights[i],heights[j])
                area = height*(j-i)
                res = max(res,area)
        return res