class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        recolor = 0
        res = k
        for right in range(len(blocks)):
            if blocks[right]=='W':
                recolor+=1
            if right-l+1 == k:
                res = min(res,recolor)
                if blocks[l]=='W':
                    recolor-=1
                l+=1
        return res

