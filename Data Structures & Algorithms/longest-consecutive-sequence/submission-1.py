class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = sorted(nums)
        count = 1
        long = 1
        if not nums:
            return 0
        for i in range(len(n)-1):
            if n[i+1] == n[i] + 1:
                count += 1

            
            elif n[i+1] == n[i]:# if nums = [1,2,3,4,4,5]sorted than  i+1 == i so continue just by continuing
            
                continue
# 
            else:
                count = 1

            long = max(long, count)
        return long
