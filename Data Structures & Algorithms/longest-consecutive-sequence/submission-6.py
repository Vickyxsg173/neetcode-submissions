class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longestStreak = 0

        for num in nums:

    
            if num-1 not in s:
                currentNum = num
                currentStreak = 1

                while currentNum+1 in s:
                    currentNum +=1
                    currentStreak +=1

                longestStreak = max(longestStreak,currentStreak)

        return longestStreak
