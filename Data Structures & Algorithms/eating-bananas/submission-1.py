from typing import List


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function (no 'self' needed here)
        def k_works(k):
            hours = 0
            for i in piles:
                # Integer ceiling division without needing math.ceil
                hours += (i + k - 1) // k
            return hours <= h

        l = 1
        r = max(piles)

        while l < r:
            k = (l + r) // 2
            # Call helper function directly, not via 'self'
            if k_works(k):
                r = k
            else:
                l = k + 1

        return l