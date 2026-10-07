class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()

        for num in nums:
            if num in res:
                return True

            res.add(num)

        return False

#'''1 → never seen → store it
# 2 → never seen → store it
# 3 → never seen → store it
# 3 → already seen → DUPLICATE → True'''