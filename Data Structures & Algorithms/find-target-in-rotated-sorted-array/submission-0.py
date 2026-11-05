class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res =0
        for num in range(n):
            if nums[num] == target:
                return num
            # else:
                # return -1  this line will stop for one iteration so 
        return -1 