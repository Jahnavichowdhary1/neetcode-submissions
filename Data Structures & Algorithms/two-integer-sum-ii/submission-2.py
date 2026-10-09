class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
# We need a bigger sum. Because the array is sorted, move left forward to the next bigger number:
            elif total < target:
                left += 1

            else:
                right -= 1
              