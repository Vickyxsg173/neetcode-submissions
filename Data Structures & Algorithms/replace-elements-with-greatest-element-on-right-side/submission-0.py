class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        promax = 0
        for i in range(0,len(arr)):
            promax = 0
            for j in range(i+1,len(arr)):
                if arr[j]>promax:
                    promax = arr[j]
                arr[i] = promax

        arr[-1] = -1
        return arr