class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1

        # Left products
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        # Right products
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res